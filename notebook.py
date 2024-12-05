from datetime import datetime
def show_menu():
    print("\n简单记事本")
    print("1. 添加新笔记")
    print("2. 查看所有笔记")
    print("3. 删除所有笔记")
    print("4. 搜索笔记")
    print("5. 删除指定笔记")
    print("0. 退出程序")
def add_note():
    note = input("请输入新的笔记内容: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open('notes.txt','r') as file:
            notes = file.readlines()
            note_id = len(notes) +1
    except FileNotFoundError:
        note_id = 1
    with open('notes.txt', 'a') as file:
        file.write(f"{note_id}.[{timestamp}] {note}\n")
    print(f"笔记已成功添加.(编号{note_id})")
def view_all_notes():
    try:
       with open('notes.txt','r') as file:
            notes = file.readlines()
            if notes:
               print("\n所有笔记:")
               for note in notes:
                   print('- ' + note.strip())
            else:
                print("没有任何笔记.")
    except FileNotFoundError:
        print("文件不存在.")
def delete_all_notes():
    with open('notes.txt', 'w'):
        pass
    print("所有笔记已被清空.")
def delete_note_by_id():
    try:
        with open('notes.txt','r') as file:
            notes = file.readlines()
        if not notes:
            print("没有任何笔记.")
            return
        view_all_notes()
        note_id = input("请输入要删除的笔记编号: ")
        notes = [note for note in notes if not note.startswith(f"{note_id}.")]
        with open('notes.txt', 'w') as file:
            file.writelines(notes)
        print(f"笔记{note_id}已成功删除.")
    except FileNotFoundError:
        print('尚无笔记记录.')



def search_notes():
    keyword = input("请输入关键字: ")
    try:
        with open('notes.txt','r') as file:
            notes = file.readlines()
            found = False
            print('\n搜索结果：')
            for note in notes:
                if keyword.lower() in note.lower():
                    print('- ' + note.strip())
                    found = True
            if not found:
                print("未找到匹配的笔记.")
    except FileNotFoundError:
        print("文件不存在.")

def main():
    while True:
        show_menu()
        choice = input("\n请选择操作 (0/1/2/3/4/5): ")
        if choice == '1':
            add_note()
        elif choice == '2':
            view_all_notes()
        elif choice == '3':
            delete_all_notes()
        elif choice == '4':
            search_notes()
        elif choice == '5':
            delete_note_by_id()
        elif choice == '0':
            break
        else:
            print("无效的选项, 请重新选择.")

if __name__ == "__main__":
    main()