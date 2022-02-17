f_txt = open("ori.txt", "r")
f_srt = open("converted.srt", "w")

cnt = 1
line = f_txt.readline()
while True:
    next_line = f_txt.readline()
    start_time = line[0:8]

    if not next_line:
        start_time_sec = int(line[6:8])
        start_time_mnt = int(line[3:5])
        start_time_hr = int(line[0:2])
        end_time_sec = start_time_sec + 4
        end_time_mnt = start_time_mnt
        end_time_hr = start_time_hr
        if end_time_sec >= 60:
            end_time_sec -= 60
            start_time_mnt += 1
            if end_time_mnt >= 60:
                end_time_mnt -= 60
                start_time_hr += 1
        end_time = str(end_time_hr).zfill(2) + ":" + str(end_time_mnt).zfill(2) + ":" + str(end_time_sec).zfill(2)
    else:
        end_time = next_line[0:8]

    out_line = str(cnt) + "\n"
    out_line = out_line + start_time + " --> " + end_time + "\n"
    out_line = out_line + line[9:-1] + "\n"

    print(out_line, file = f_srt)

    if not next_line:
        break

    line = next_line
    cnt += 1
