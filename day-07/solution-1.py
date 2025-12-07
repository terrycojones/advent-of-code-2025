from lib import read_data

width, beam, row_splitters = read_data()
split_count = 0
beams = {beam}

for splitters in row_splitters:
    next_beams = set()
    for beam in beams:
        if beam in splitters:
            split_count += 1
            if beam - 1 >= 0:
                next_beams.add(beam - 1)
            if beam + 1 < width:
                next_beams.add(beam + 1)
        else:
            next_beams.add(beam)
    beams = next_beams


print(split_count)
