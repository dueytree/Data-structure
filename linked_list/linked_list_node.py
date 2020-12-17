class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, data):
        self.data = data  # 실제 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스


class LinkedList:
    """링크드 리스트 클래스"""

    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def prepend(self, data):
        """링크드 리스트의 가장 앞에 데이터 삽입"""
        # 코드를 쓰세요
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            head = self.head
            self.head = new_node
            self.head.next = head

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += f" {iterator.data} |"
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str

    # # 새로운 링크드 리스트 생성
    # linked_list = LinkedList()
    #
    # # 여러 데이터를 링크드 리스트 앞에 추가
    # linked_list.prepend(11)
    # linked_list.prepend(7)
    # linked_list.prepend(5)
    # linked_list.prepend(3)
    # linked_list.prepend(2)
    #
    # print(linked_list)  # 링크드 리스트 출력
    #
    # # head, tail 노드가 제대로 설정됐는지 확인
    # print(linked_list.head.data)
    # print(linked_list.tail.data)
    #

    def pop_left(self):
        """링크드 리스트의 가장 앞 노드 삭제 메소드. 단, 링크드 리스트에 항상 노드가 있다고 가정한다"""
        data = self.head.data  # 삭제할 노드를 미리 저장해놓는다

        # 지우려는 데이터가 링크드 리스트의 마지막 남은 데이터일 때
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return data  # 삭제된 노드의 데이터를 리턴한다

# # 새로운 링크드 리스트 생성
# linked_list = LinkedList()
#
# # 여러 데이터를 링크드 리스트 앞에 추가
# linked_list.prepend(11)
# linked_list.prepend(9)
# linked_list.prepend(5)
# linked_list.prepend(3)
# linked_list.prepend(2)
#
# print(linked_list) # 링크드 리스트 출력
#
# # 가장 앞 노드 계속 삭제
# print(linked_list.pop_left())
# print(linked_list.pop_left())
# print(linked_list.pop_left())
# print(linked_list.pop_left())
# print(linked_list.pop_left())
#
# print(linked_list) # 링크드 리스트 출력
# print(linked_list.head)
# print(linked_list.tail)