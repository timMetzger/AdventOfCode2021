# Timothy Metzger
# Advent of Code 2021
# Day 16

def main():
    with open('inputs/day16.txt') as f:
        packet = f.readline().strip()

    binary_representation = bin(int(packet,16))[2:]
    print(binary_representation)

    # This is my garbage solution that only works sometimes
    # I think that it is an issue with the way that I parse the input because in the examples
    # given i have a different binary value than the example but when converting from hex to binary
    # manually I am getting the correct value

    # TODO in the future split up the functions for the parsing
    # Part 1:
    # Bits (0-2) - packet version
    # Bits (3-5) - type ID
    #       If type ID == 4 -> literal value (encodes a single binary number)
    #       Binary number is padded with 0's (right side) until length is a multiple of 4 bits
    #       All groups of 4 expect for the last group of 4 lead with a 1 ie 10111 (so really groups of 5)
    #
    #       If type ID != 4 -> operator
    #       length type Id directly proceeds the type ID
    #       if length_type_ID == 0 -> next 15 bits are a number that represents the total length in bits
    #       if length_type_ID == 1 -> next 11 bits are a number that represents the number of sub-packets

    decode(binary_representation, [], 0, 0)


def decode(binary_code, nums, pos, version_sum):
    try:
        packet_version = int(binary_code[pos:pos + 3], 2)
        type_id = int(binary_code[pos + 3:pos + 6], 2)
        version_sum += packet_version
        pos += 6
        if type_id == 4:
            return get_literal(binary_code, pos)

        else:

            length_type_id = int(binary_code[pos])
            pos += 1

            if length_type_id == 0:
                subpacket_length = int(binary_code[pos:pos + 13], 2)
                pos += 13

                while pos < pos + subpacket_length:
                    val, pos = decode(binary_code, nums, pos,version_sum)
                    nums.append(int(val, 2))


            else:
                number_of_subpackets = int(binary_code[pos:pos + 11], 2)
                pos += 11
                n = 0
                while n < number_of_subpackets:
                    val, pos = decode(binary_code, nums, pos,version_sum)
                    nums.append(int(val, 2))
                    n += 1
                    
        print(version_sum,nums)

    except IndexError:
        print(version_sum,nums)





def get_literal(binary, pos):
    value = ''
    next_bit = binary[pos]

    while next_bit == '1':
        value += binary[pos + 1:pos + 5]
        pos += 5
        next_bit = binary[pos]
    value += binary[pos + 1:pos + 5]
    pos += 5


    return value, pos



# Solution from reddit
#     input = open('inputs/day16.txt').read().splitlines()[0]
#     bin_input = ''.join(format(int(char, base=16), '#06b')[2:] for char in input)
#     print(parse_packet(bin_input)[-1])
# def product(values):
#     prod = 1
#     for value in values:
#         prod *= value
#     return prod
#
#
# def gt(values):
#     return int(values[0] > values[1])
#
#
# def lt(values):
#     return int(values[0] < values[1])
#
#
# def equals(values):
#     return int(values[0] == values[1])
#
#
# def parse_literals(binary):
#     i = 6
#     total = ''
#     while True:
#         total += binary[i + 1:i + 5]
#         if binary[i] == '0':
#             return i + 5, int(total, 2)
#         i += 5
#
#
# def parse_operation(binary, operation):
#     values = []
#     if binary[6] == '1':
#         i = 18
#         for _ in range(int(binary[7:18], 2)):
#             j, value = parse_packet(binary[i:])
#             i += j
#             values.append(value)
#     elif binary[6] == '0':
#         i = 22
#         while i < 22 + int(binary[7:22], 2):
#             j, value = parse_packet(binary[i:])
#             i += j
#             values.append(value)
#     return i, operation(values)
#
#
# def parse_packet(binary):
#     id = int(binary[3:6], 2)
#     if id == 4:
#         return parse_literals(binary)
#     else:
#         operations = {0: sum, 1: product, 2: min, 3: max, 5: gt, 6: lt, 7: equals}
#         return parse_operation(binary, operations[id])





if __name__ == "__main__":
    main()
