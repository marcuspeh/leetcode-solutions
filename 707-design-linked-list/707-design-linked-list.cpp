struct Node {
    int val;
    Node* next;
    Node* prev;
    
    Node(int val) {
        this->val = val;
        this->next = nullptr;
    }
    
    Node(int val, Node* prev, Node* next) {
        this->val = val;
        this->prev = prev;
        this->next = next;
    }
};

class MyLinkedList {
private:
    int length;
    Node* head;
    Node* tail;
public:
    MyLinkedList() {
        this->length = 0;
        this->head = new Node(0);
        this->tail = new Node(0);
        this->head->next = this->tail;
        this->tail->prev = this->head;
    }
    
    int get(int index) {
        if (index >= this->length || index < 0) {
            return -1;
        }
        
        Node* curr = this->head;
        for (int i = 0; i <= index; i++) {
            curr = curr->next;
        }
        return curr->val;
    }
    
    void addAtHead(int val) {
        addAtIndex(0, val);
    }
    
    void addAtTail(int val) {
        addAtIndex(this->length, val);
    }
    
    void addAtIndex(int index, int val) {
        if (index > this->length || index < 0) {
            return;
        }
        
        Node* curr = this->head;
        for (int i = 0; i < index; i++) {
            curr = curr->next;
        }
        
        Node* newNode = new Node(val, curr, curr->next);
        curr->next = newNode;
        newNode->next->prev = newNode;

        this->length++;
    }
    
    void deleteAtIndex(int index) {
        if (index >= this->length || index < 0) {
            return;
        }
        if (this->length == 0) {
            return;
        }
        
        Node* curr = this->head;
        for (int i = 0; i <= index; i++) {
            curr = curr->next;
        }
        
        Node* toRemove = curr;
        toRemove->prev->next = toRemove->next;
        toRemove->next->prev = toRemove->prev;

        // delete toRemove;
        this->length--;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */