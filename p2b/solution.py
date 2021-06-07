# versions = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
# versions2 = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
#

def solution(l):
    # ===== Step 1: Split the version by "." to get list of numbers, and typecast to int for sorting =====
    version_table = [[int(num) for num in version.split('.')] for version in l]

    # ===== Step 2: Sort the version table, and convert it back to a string =====
    sorted_version_table = sorted(version_table)
    sorted_version_table = [[str(version) for version in full_version] for full_version in sorted_version_table]

    # ===== Step 3: Convert it back to string and return =====
    return ','.join(['.'.join(full_version) for full_version in sorted_version_table])

