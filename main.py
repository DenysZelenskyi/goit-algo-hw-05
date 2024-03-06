import timeit

from functions import kmp_search, boyer_moore_search, rabin_karp_search


if __name__ == '__main__':
    def read_file(filename):
        try:
            with open(filename, 'r', encoding='cp1251') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            print(f"Файл '{filename}' не знайдено.")
            return None

    filename1 = 'article1.txt'  
    filename2 = 'article2.txt'  
    main_string1 = read_file(filename1)
    main_string2 = read_file(filename2)
    real_pattern = 'Висновки. '
    fake_pattern = 'dffs99'


    tsr_kmp1 = timeit.timeit(lambda: kmp_search(main_string1, real_pattern), number=100)
    tsr_boy1 = timeit.timeit(lambda: boyer_moore_search(main_string1, real_pattern), number=100)
    tsr_rab1 = timeit.timeit(lambda: rabin_karp_search(main_string1, real_pattern), number=100)

    tsf_kmp1 = timeit.timeit(lambda: kmp_search(main_string1, fake_pattern), number=100)
    tsf_boy1 = timeit.timeit(lambda: boyer_moore_search(main_string1, fake_pattern), number=100)
    tsf_rab1 = timeit.timeit(lambda: rabin_karp_search(main_string1, fake_pattern), number=100)


    tsr_kmp2 = timeit.timeit(lambda: kmp_search(main_string2, real_pattern), number=100)
    tsr_boy2 = timeit.timeit(lambda: boyer_moore_search(main_string2, real_pattern), number=100)
    tsr_rab2 = timeit.timeit(lambda: rabin_karp_search(main_string2, real_pattern), number=100)

    tsf_kmp2 = timeit.timeit(lambda: kmp_search(main_string2, fake_pattern), number=100)
    tsf_boy2 = timeit.timeit(lambda: boyer_moore_search(main_string2, fake_pattern), number=100)
    tsf_rab2 = timeit.timeit(lambda: rabin_karp_search(main_string2, fake_pattern), number=100)


    print(f"| {'    Algorithm':<20} | {'     Article 1':<23} | {'     Article 2':<23} |")
    print(f"| {' '*20} | {'-'*10} | {'-'*10} | {'-'*10} | {'-'*10} |")
    print(f"| {' ':<20} | {'  Real':<10} | {'  Fake':<10} | {'  Real':<10} | {'  Fake':<10} |")
    print(f"| {'-'*20} | {'-'*10} | {'-'*10} | {'-'*10} | {'-'*10} |")
    print(f"| {'kmp search':<20} | {tsr_kmp1:10f} | {tsf_kmp1:10f} | {tsr_kmp2:10f} | {tsf_kmp2:10f} |")
    print(f"| {'boyer moore search':<20} | {tsr_boy1:10f} | {tsf_boy1:10f} | {tsr_boy2:10f} | {tsf_boy2:10f} |")
    print(f"| {'rabin karp search':<20} | {tsr_rab1:10f} | {tsf_rab1:10f} | {tsr_rab2:10f} | {tsf_rab2:10f} |")