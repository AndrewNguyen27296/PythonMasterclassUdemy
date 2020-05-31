'''
Viết chương trình thực hiện việc xử lý từ điển Anh – Việt như sau:

- Tạo một từ điển (key: từ tiếng Anh, value: list nhiều nghĩa Tiếng Việt)
ví dụ: check: tờ séc, hóa đơn, kiểm tra, chiếu cờ tướng

=> Chương trình sẽ thực hiện những công việc sau:
- Hiển thị từ điển, cho biết trong từ điển hiện tại có bao nhiêu từ
- Thêm từ vào từ điển, và hiển thị từ điển sau khi thêm
- Tìm kiếm từ tiếng Anh => nếu tìm thấy thì hiển thị key và value.
Nếu không tìm thấy thì thông báo không tìm thấy
- Xóa một từ trong từ điển, dựa trên key cung cấp , và hiển thị từ điển sau khi xóa
'''

dictionary = {'work': ['công việc', 'việc làm', 'tác phẩm'], 'bark': ['vỏ cây', 'tiếng sủa', 'thuyền ba cột buồm'],
              'bat': ['con dơi', 'gậy', 'đánh bóng'], 'board': ['bảng', 'ban quản lý', 'lên tàu'],
              'bowl': ['cái bát', 'khán đài', 'quả bóng quần'], 'stamp': ['con tem', 'phiếu mua hàng', 'con dấu'],
              'club': ['câu lạc bộ', 'gậy đánh golf', 'dùi cui']}

index = 1
while index == 1:
    choice = int(input('What do you want to do? 0: Exit, 1: Dictionary list; 2: Search, 3: Add, 4: Delete: '))

    if choice == 0:
        exit

    if choice == 1:
        print('Dictionary:')
        print('English \t Vietnamese')

        for key in dictionary:
            print(key, "\t:", dictionary.get(key))

    elif choice == 2:
        name_search = input('Input word to search:\t')
        found_word = dictionary.get(name_search)
        if found_word is None:
            print("There is no translation for:", name_search)
        else:
            print("Found:", name_search, "\nVietnamese meaning:", found_word)

    elif choice == 3:
        new_eng = input('Input English word:\t')
        meaning_list = []
        while True:
            meaning = input('Input translation (press 0 to stop):')
            if meaning == "0":
                break
            meaning_list.append(meaning)
        dictionary[new_eng] = meaning_list
        print('Dictionary:')
        print('English \t Vietnamese')

        for key in dictionary:
            print(key, "\t:", dictionary.get(key))

    elif choice == 4:
        word_delete = input('Input English word you want to delete:')
        x = int(input('Are you sure? 1: Delete, 0: Cancel\t'))
        if x == 0:
            print('Dictionary:')
            print('English \t Vietnamese')

            for key in dictionary:
                print(key, "\t:", dictionary.get(key))
        elif x == 1:
            del dictionary[word_delete]
