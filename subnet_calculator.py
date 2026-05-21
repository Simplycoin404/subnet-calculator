cidr = int(input("Enter CIDR number: "))

hosts = (2 ** (32 - cidr)) - 2
total_addresses = 2 ** (32 - cidr)

subnet_masks = {
    8: "255.0.0.0",
    16: "255.255.0.0",
    24: "255.255.255.0",
    25: "255.255.255.128",
    26: "255.255.255.192",
    27: "255.255.255.224",
    28: "255.255.255.240"
}

print(f"\nCIDR: /{cidr}")

if cidr in subnet_masks:
    print(f"Subnet Mask: {subnet_masks[cidr]}")
else:
    print("Subnet Mask: Not in simple database")

print(f"Total Addresses: {total_addresses}")
print(f"Usable Hosts: {hosts}")
