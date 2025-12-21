import sys

def hex_to_dec(hex_str):
    return int(hex_str, 16)

def dec_to_hex(num):
    return f"{num:02X}"

def get_possible_positions(guess):
    try:
        GuessedData=guess.strip().split()
        guess_pos = GuessedData[0]
        dist=GuessedData[1]
        if len(guess_pos) != 4 or len(dist) != 4:
            return set()
        int(guess_pos, 16)
        int(dist, 16)
    except (ValueError, IndexError):
        return set()
    
    guess_row_hex = guess_pos[:2]
    guess_col_hex = guess_pos[2:]
    dist_h_hex = dist[:2]
    dist_v_hex = dist[2:]
    
    guess_row = hex_to_dec(guess_row_hex)
    guess_col = hex_to_dec(guess_col_hex)
    dist_h = hex_to_dec(dist_h_hex)
    dist_v = hex_to_dec(dist_v_hex)
    
    possible = set()
    offsets = [
        (dist_h, dist_v), (-dist_h, dist_v),
        (dist_h, -dist_v), (-dist_h, -dist_v),
        (dist_v, dist_h), (-dist_v, dist_h),
        (dist_v, -dist_h), (-dist_v, -dist_h)
    ]
    for dr, dc in offsets:
        new_row = guess_row + dr
        new_col = guess_col + dc
        if 0 <= new_row <= 255 and 0 <= new_col <= 255:
            pos = (dec_to_hex(new_row), dec_to_hex(new_col))
            possible.add(pos)
    return possible

def solve_case(input_lines):
    if len(input_lines) != 3:
        return None
    pos1 = get_possible_positions(input_lines[0])
    pos2 = get_possible_positions(input_lines[1])
    pos3 = get_possible_positions(input_lines[2])
    common = pos1 & pos2 & pos3
    if common: 
        return next(iter(common))
    else: 
        return None

if __name__ == "__main__":
    try:
        lines = [line.strip() for line in sys.stdin if line.strip()]
        if not lines:
            print("No input data")
            
        for i in range(0, len(lines), 3):
            case_lines = lines[i:i+3]
            result = solve_case(case_lines)
            if result:
                row, col = result
                print(f"({row},{col})")
            else:
                print("No commom location found")
    except Exception as E:
        print(f"{type(E).__name__} - {str(E)}")
        