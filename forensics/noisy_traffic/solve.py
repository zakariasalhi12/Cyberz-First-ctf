from scapy.all import rdpcap, Raw, IP, TCP

def extract_real_data_with_seq(pcap_file, output_file):
    packets = rdpcap(pcap_file)

    real_data_chunks = []

    seq_dict = {}

    real_src = "10.0.0.1"
    real_dst = "10.0.0.2"

    for pkt in packets:
        if pkt.haslayer(IP) and pkt.haslayer(TCP):
            src_ip = pkt[IP].src
            dst_ip = pkt[IP].dst

            if (src_ip == real_src and dst_ip == real_dst) or (src_ip == real_dst and dst_ip == real_src):
                if pkt.haslayer(Raw):
                    seq_num = pkt[TCP].seq

                    raw_data = pkt[Raw].load
                    if seq_num not in seq_dict:
                        seq_dict[seq_num] = raw_data
                    else:
                        seq_dict[seq_num] += raw_data

                    print(f"Extracted {len(raw_data)} bytes of data from packet with seq {seq_num}.")

    sorted_seq = sorted(seq_dict.keys())

    with open(output_file, "wb") as f:
        for seq in sorted_seq:
            f.write(seq_dict[seq])
    
    print(f"Reassembled file saved to {output_file}")

pcap_file = "noisy_traffic.pcap"
output_file = "reassembled_file.png"

extract_real_data_with_seq(pcap_file, output_file)
