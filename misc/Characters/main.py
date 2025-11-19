import socket
import threading

FLAG = "CTF{l0r3m_1p5um_d0l0r_517_4m37_c0n53c737ur_4d1p151c1n6_3l17._1d_duc1mu5_n3m0,_p0551mu5_0ff1c115_0mn15_cumqu3_fu64_37_m46n4m!_h1c_34_34rum_pr0v1d3n7,_1573_d0l0rum_qu0d_357_f4c1l15_c0mm0d1_3x_cum!}" 

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
