import socket
import threading

FLAG = "CTF{th1s_1s_4_r3v3rs3_0r4cl3}"  # <-- change this!

def handle_client(conn, addr):
    conn.sendall(b"Which character (index) of the flag do you want? Enter an index: ")

    try:
        while True:
            data = conn.recv(1024).strip()
            if not data:
                break

            try:
                idx = int(data.decode())
                if 0 <= idx < len(FLAG):
                    response = f"Character at Index {idx}: {FLAG[idx]}\n"
                else:
                    response = "Invalid index\n"
            except ValueError:
                response = "Please enter a number\n"

            conn.sendall(response.encode())
            conn.sendall(b"Which character (index) of the flag do you want? Enter an index: ")

    except Exception:
        pass
    finally:
        conn.close()


def main():
    host = "0.0.0.0"
    port = 5000  # change for deployment

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)

    print(f"Listening on {host}:{port}")

    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()


if __name__ == "__main__":
    main()
