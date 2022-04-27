input_version = input().split(".")
full_str = ''

for i in input_version:
    full_str += i

new_version = int(full_str) + 1

version = []

for n in str(new_version):
    version.append(n)

print('.'.join(str(s) for s in version))
