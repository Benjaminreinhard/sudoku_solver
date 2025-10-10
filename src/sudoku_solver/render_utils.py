# Constants
# ---------
HEADER = "\033[95m"
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
ENDC = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"


# Functions
# ---------


def font_style(label, styles, enabled):
    if enabled:
        for style in styles:
            label = f"{style}{label}{ENDC}"

    return label


def title_print(label, enabled):
    print(font_style(label, [BOLD, BLUE], enabled))


def fill_to_width(label, width):
    return label[:width] + " " * (width - len(label))


def render_states(state_infos, coloring_enabled):
    num_of_states = len(state_infos)
    width = 11 * 2
    space_between = " " * 5

    headers = []
    for x in range(num_of_states):
        h = state_infos[x]["header"] if "header" in state_infos[x] else ""
        headers += [h]

    if any(headers):
        header = ""
        for h in headers:
            header += fill_to_width(h + ": ", width) + space_between
        print(f"{header}\n")

    horizontal_line = ("------+-------+-------" + space_between) * num_of_states

    for i in range(9):
        row = ""
        for x in range(num_of_states):
            state = state_infos[x]["state"]
            if "comparison_state" in state_infos[x]:
                comparison_state = state_infos[x]["comparison_state"]
            else:
                comparison_state = state

            state_row = ""
            for j in range(9):
                if j in [3, 6]:
                    state_row += "| "

                if state[i][j] == 0:
                    state_row += ". "
                else:
                    entry = f"{state[i][j]} "
                    if state[i][j] != comparison_state[i][j]:
                        entry = font_style(entry, [GREEN], coloring_enabled)
                    state_row += entry

            row += state_row + space_between

        if i in [3, 6]:
            print(horizontal_line)

        print(row)
    print()

    footers = []
    for x in range(num_of_states):
        f = state_infos[x]["footer"] if "footer" in state_infos[x] else []
        footers += [f]

    if any(footers):
        max_index = max([len(f) for f in footers])

        footer = ""
        for index in range(max_index):
            for f in footers:
                label = f[index] if index < len(f) else ""
                footer += fill_to_width(label, width) + space_between
            footer += "\n"
        print(footer)


def render_counts_of_used_tricks(trick_order, outline):
    counts = {}
    for trick in trick_order:
        counts[trick.__name__] = 0

    for situation in outline:
        name = situation["next_trick"]
        if name is None:
            continue
        counts[name] += len(situation["cells_with_numbers"][name])

    formatted_counts = []
    for name in counts:
        formatted_counts += [f"{name}: {counts[name]}"]

    width = max(map(len, formatted_counts)) + 2
    counts_in_print_format = ""
    for count in formatted_counts:
        counts_in_print_format += fill_to_width(count, width)
    counts_in_print_format += "\n"

    print(counts_in_print_format)


def render_counts_of_available_steps(trick_order, outline, num_of_entries_per_row):
    def format_entry(x):
        return fill_to_width(str(x) if x > 0 else ".", 4)

    def format_row(label, lst):
        return f"{fill_to_width(label, sidebar_width)}| {''.join(lst)}"

    def horizontal_line(n):
        return f"{'-' * sidebar_width}+-{'-' * n * entry_width}"

    def ceil(x):
        return int(x) if x - int(x) == 0 else int(x) + 1

    formatted_counts = {}
    for trick in trick_order:
        formatted_counts[trick.__name__] = []
    formatted_counts["total"] = []

    entry_width = 4

    for situation in outline:
        total = 0
        for trick in trick_order:
            name = trick.__name__
            count = len(situation["cells_with_numbers"][name])
            total += count
            formatted_counts[name] += [format_entry(count)]

        formatted_counts["total"] += [format_entry(total)]

    sidebar_width = 10

    num_of_counts = len(formatted_counts["total"])

    num_of_blocks = ceil(num_of_counts / num_of_entries_per_row)

    for block_nr in range(num_of_blocks):
        a = block_nr * num_of_entries_per_row
        n = min(num_of_entries_per_row, num_of_counts - a)

        print(format_row("Iteration", [format_entry(x) for x in range(a, a + n)]))

        print(horizontal_line(n))

        for trick in trick_order:
            name = trick.__name__
            print(format_row(name, formatted_counts[name][a : a + n]))

        print(horizontal_line(n))

        print(format_row("Total", formatted_counts["total"][a : a + n]))

        print()
