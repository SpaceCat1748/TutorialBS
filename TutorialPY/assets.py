import argparse
import io
import json
import os
import pathlib
import socket
import sys
import urllib.parse
import urllib.request
import zlib
import concurrent.futures

SC_GAME = {
    "bs": {
        "address": ("game.brawlstarsgame.com", 9339),
        "assetsUrl": "http://game-assets.brawlstarsgame.com",
        "protocol": 2,
        "keyVersion": 19,
        "majorVersion": 32,
        "minorVersion": 0,
        "build": 170,
        "contentHash": "a241cb6a716506dfc59517a75e7236ce93d56206",
    },
    "cr": {
        "address": ("game.clashroyaleapp.com", 9339),
        "assetsUrl": "http://game-assets.clashroyaleapp.com",
        "protocol": 2,
        "keyVersion": 14,
        "majorVersion": 3,
        "minorVersion": 0,
        "build": 3074,
        "contentHash": "c897e2c48dfa342f1470ad1b06a3e71e2f809b65",
    },
    "coc": {
        "address": ("gamea.clashofclans.com", 9339),
        "assetsUrl": "http://game-assets.clashofclans.com",
        "protocol": 3,
        "keyVersion": 22,
        "majorVersion": 13,
        "minorVersion": 0,
        "build": 675,
        "contentHash": "df960a35d591b610bf7aa6f37f9380bc28cda683",
    },
    "hd": {
        "address": ("game.haydaygame.com", 9339),
        "assetsUrl": "http://game-assets.haydaygame.com",
        "protocol": 0,
        "keyVersion": 0,
        "majorVersion": 1,
        "minorVersion": 0,
        "build": 49,
        "contentHash": "32b1a85e0122a62f2dca8f46e5479cec47b0ea96",
    },
}


def handshake(game):
    payload = b""
    payload += game["protocol"].to_bytes(4, byteorder="big")
    payload += game["keyVersion"].to_bytes(4, byteorder="big")
    payload += game["majorVersion"].to_bytes(4, byteorder="big")
    payload += game["minorVersion"].to_bytes(4, byteorder="big")
    payload += game["build"].to_bytes(4, byteorder="big")
    payload += b"\xff\xff\xff\xff"  # contentHash
    payload += (2).to_bytes(4, byteorder="big")  # deviceType
    payload += (2).to_bytes(4, byteorder="big")  # appStore

    header = b""
    header += (10100).to_bytes(2, byteorder="big")
    header += len(payload).to_bytes(3, byteorder="big")
    header += (0).to_bytes(2, byteorder="big")

    return header + payload


def client_handshake(game):
    def recv_until(sock, size):
        buf = b""
        while len(buf) != size:
            buf += sock.recv(size - len(buf))
        return io.BytesIO(buf)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SC_GAME[game]["address"])
    msg_handshake = handshake(SC_GAME[game])
    s.send(msg_handshake)

    header = recv_until(s, 7)
    id = int.from_bytes(header.read(2), byteorder="big")
    length = int.from_bytes(header.read(3), byteorder="big")
    header.read(2)

    payload = recv_until(s, length)

    if game == "bs":
        return handle_bb(id, payload)
    elif game == "bs":
        return handle_cr(id, payload)

    return None, None


def handle_bb(id, payload):
    msg_type = int.from_bytes(payload.read(1), byteorder="big")
    if id != 20103 or msg_type != 7:
        print("Downloading..")
        return None, None

    fingerprint_length = int.from_bytes(payload.read(4), byteorder="big")
    fingerprint = payload.read(fingerprint_length).decode("utf-8")

    payload.read(25)

    assets_url_length = int.from_bytes(payload.read(4), byteorder="big")
    assets_url = payload.read(assets_url_length).decode("utf-8")

    return assets_url, json.loads(fingerprint)

def dowload_fingerprint(game):
    url = (
        SC_GAME[game]["assetsUrl"]
        + "/"
        + SC_GAME[game]["contentHash"]
        + "/fingerprint.json"
    )
    with urllib.request.urlopen(url, timeout=10) as conn:
        data = conn.read()

    return json.loads(data)


def download_asset(assets_url, rel_file_path, output_dir):
    sub_dirs, file_name = os.path.split(rel_file_path)
    file_path = os.path.join(output_dir, file_name)
    
    try:
        url = assets_url + "/" + rel_file_path
        with urllib.request.urlopen(url, timeout=10) as conn:
            data = conn.read()
        with open(file_path, "wb") as f:
            f.write(data)
    except Exception as e:
        return f"{e}"

    return "downloaded"


def down(game, thread_count, output_dir):
    assets_url = fingerprint = None

    if game in SC_GAME:
        assets_url, fingerprint = client_handshake(game)
    if not assets_url or not fingerprint:
        assets_url = SC_GAME[game]["assetsUrl"]
        fingerprint = dowload_fingerprint(game)

    assets_url = urllib.parse.urljoin(assets_url, fingerprint["sha"])

    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_count) as executor:
        futures = {}
    for fp in fingerprint["files"]:
        rel_file_path1 = fp["file"]
        if "/" in rel_file_path1:
            slash_index = rel_file_path1.index('/')
            filename = rel_file_path1[slash_index + 1:]
            if filename == "tutorial.csv":
                download_asset(assets_url, rel_file_path1, "./defolt/files")
            if filename == "characters.csv":
                download_asset(assets_url, rel_file_path1, "./defolt/files")

down("bs", 4, "./defolt/files")
