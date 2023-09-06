from os import cpu_count

max_threads = min(32, cpu_count() + 4)
main_threads = 2
