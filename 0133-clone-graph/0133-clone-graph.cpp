/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
    Node* replicateNode(Node* node, unordered_map<int, Node*>& cache) {
        if (cache.count(node->val) > 0) {
            return cache[node->val];
        }
        Node* newNode = new Node(node->val);
        cache[node->val] = newNode;
        
        for (auto neighbor: node->neighbors) {
            Node* newNeighbor = replicateNode(neighbor, cache);
            newNode->neighbors.push_back(newNeighbor);
        }
        return newNode;
    }
public:
    Node* cloneGraph(Node* node) {
        if (node == nullptr) {
            return node;
        }
        unordered_map<int, Node*> cache;
        return replicateNode(node, cache);        
    }
};