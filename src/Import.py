from src import Converter, Parameter


def read_ini():
    f = open("Gear.ini")
    for line in f:
        if line.__contains__('folder:'):
            folder = line[8:].rstrip()
        if line.__contains__('control_file:'):
            control_file = line[14:].rstrip()
    f.close()
    return folder + control_file


def extract_value_from_line(line):
    index = line.find("** ")
    return line[5:index - 1].strip()


def read_ste(filename):
    content = {}
    f = open(filename)
    for line in f:
        if line.__contains__('*1001'):
            content.update({"number of teeth": int(extract_value_from_line(line))})
        if line.__contains__('*1101'):
            content.update({"normal module": float(extract_value_from_line(line))})
        if line.__contains__('*1104'):
            content.update({"helix angle": Converter.grad2rad(float(extract_value_from_line(line)))})
            if content["helix angle"] < Parameter.Precision.eps_normal:
                content.update({"helix angle direction": Parameter.DirectionHelixAngle.LEFT})
            else:
                content.update({"helic angle direction": Parameter.DirectionHelixAngle.RIGHT})
        if line.__contains__('*1106'):
            content.update({"gear width": float(extract_value_from_line(line))})
        if line.__contains__('*1107'):
            content.update({"addendum modification factor": float(extract_value_from_line(line))})
        if line.__contains__('*1109'):
            content.update({"tip diameter": float(extract_value_from_line(line))})
        if line.__contains__('*1110'):
            content.update({"root diameter generated": float(extract_value_from_line(line))})
        if line.__contains__('*1111'):
            content.update({"normal pressure angle left": Converter.grad2rad(float(extract_value_from_line(line)))})
        if line.__contains__('*1112'):
            content.update({"normal pressure angle right": Converter.grad2rad(float(extract_value_from_line(line)))})
        if line.__contains__('*1127'):
            content.update({"number of measuring teeth": int(extract_value_from_line(line))})
        if line.__contains__('*1128'):
            content.update({"tooth span": float(extract_value_from_line(line))})
        if line.__contains__('*1129'):
            content.update({"ball diameter": float(extract_value_from_line(line))})
        if line.__contains__('*1130'):
            content.update({"measurement over balls": float(extract_value_from_line(line))})
    f.close()
    if ("normal pressure angle left" in content) and not ("normal pressure angle right" in content):
        content.update({"normal pressure angle right": content["normal pressure angle left"]})
    if not("normal pressure angle left" in content) and ("normal pressure angle right" in content):
        content.update({"normal pressure angle left": content["normal pressure angle right"]})
    return content
