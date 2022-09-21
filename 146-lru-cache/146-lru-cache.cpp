class Node {
public:
    int key;
    int val;
    Node* next;
    Node* prev;
    
    Node(int key, int val) {
        this->key = key;
        this->val = val;
        this->prev = nullptr;
        this->next = nullptr;
    }
};

class LRUCache {
private:
    Node* head;
    Node* tail;
    unordered_map<int, Node*> cache;
    int capacity;
    
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
        this->head = new Node(0, 0);
        this->tail = new Node(0, 0);
        this->head->next = this->tail;
        this->tail->prev = this->head;
    }
    
    int get(int key) {
        if (this->cache.find(key) == this->cache.end()) {
            return -1;
        }
        
        Node* node = remove(cache[key]);
        insert(node);
        return node->val;
    }
    
    void put(int key, int value) {
        if (this->cache.find(key) != this->cache.end()) {
            Node* node = remove(cache[key]);
            node->val = value;
            insert(node);
            return;
        }
        
        Node* node = new Node(key, value);        
        insert(node);
        cache[key] = node;
        
        if (cache.size() > this->capacity) {
            cache.erase(this->tail->prev->key);
            Node* toRemove = remove(this->tail->prev);
            // delete toRemove;
        }
    }
    
    Node* remove(Node* node) { // return value
        node->prev->next = node->next;
        node->next->prev = node->prev;
        
        node->next = nullptr;
        node->prev = nullptr;
        
        return node;
    }
    
    void insert(Node* newNode) {        
        newNode->prev = this->head;
        newNode->next = this->head->next;
        
        this->head->next->prev = newNode;
        this->head->next = newNode;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */