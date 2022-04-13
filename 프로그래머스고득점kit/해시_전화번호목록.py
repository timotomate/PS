phone_book = ["119", "97674223", "1195524421"]
phone_book2 = ["123","456","789"]
phone_book3 = ["12","123","1235","567","88"]


def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1, p2)
        if p2.startswith(p1):
            return False
    return True

print(solution(phone_book))