from scapy.all import *
import os, time, random

def generate_noisy_pcap(num_parts=11, delay_seconds=10, output_file="noisy_traffic.pcap"):
    packets = []
    real_src = "10.0.0.1"
    real_dst = "10.0.0.2"

    for i in range(1, num_parts + 1):
        num_garbage = random.randint(4, 8)
        for _ in range(num_garbage):
            garbage_data = os.urandom(random.randint(50, 400))
            pkt = IP(src=f"192.168.{random.randint(0,255)}.{random.randint(1,254)}",
                     dst=f"172.16.{random.randint(0,255)}.{random.randint(1,254)}") \
                  / TCP(sport=random.randint(1000, 65000),
                        dport=random.randint(1000, 65000)) \
                  / Raw(load=garbage_data)
            packets.append(pkt)

        filename = f"part_{i:02d}.bin"
        if not os.path.exists(filename):
            print(f"[!] Warning: {filename} not found, skipping.")
            continue

        with open(filename, "rb") as f:
            data = f.read()

        pkt_real = IP(src=real_src, dst=real_dst) / \
                   TCP(sport=4000 + i, dport=8080, seq=i) / \
                   Raw(load=data)
        packets.append(pkt_real)

        print(f"[+] Added real chunk {filename} ({len(data)} bytes) with {num_garbage} fake packets before it.")


    for _ in range(random.randint(5, 10)):
        garbage_data = os.urandom(random.randint(100, 300))
        pkt = IP(src="8.8.8.8", dst="1.1.1.1") / UDP(sport=random.randint(1000, 65000), dport=53) / Raw(load=garbage_data)
        packets.append(pkt)

    wrpcap(output_file, packets)
    print(f"\n[+] Finished! Generated {len(packets)} packets into {output_file}")

# Run it
generate_noisy_pcap()
