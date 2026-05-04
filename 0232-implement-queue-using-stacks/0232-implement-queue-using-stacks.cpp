class MyQueue {
    stack<int> input;
    stack<int> output;
public:
    MyQueue() {
        
    }
    
    void push(int x) {
        input.push(x);
    }
    
    int pop() {
        if (output.size() == 0 && input.size() != 0) {
            while (input.size() != 0) {
                output.push(input.top());
                input.pop();
            }
        }

        if (output.size() != 0) {
            int topval = output.top();
            output.pop();
            return topval;
        }
        return 0;
    }
    
    int peek() {
        if (output.size() == 0 && input.size() != 0) {
            while (input.size() != 0) {
                output.push(input.top());
                input.pop();
            }
        }

        if (output.size() != 0) {
            return output.top();
        }
        return 0;
    }
    
    bool empty() {
        if (input.size() == 0 && output.size() == 0) {
            return true;
        }
        return false;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */