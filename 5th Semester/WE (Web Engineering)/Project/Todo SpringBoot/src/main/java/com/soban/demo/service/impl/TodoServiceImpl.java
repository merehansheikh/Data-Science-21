package com.soban.demo.service.impl;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.soban.demo.exception.ResourceNotFoundException;
import com.soban.demo.model.Todo;
import com.soban.demo.repository.TodoRepository;
import com.soban.demo.service.TodoService;

@Service
public class TodoServiceImpl implements TodoService {

    @Autowired
    private TodoRepository todoRepository;

    @Override
    public List<Todo> findAll() {
        return todoRepository.findAll();
    }

    @Override
    public Todo findById(String id) {
        return todoRepository.findById(id).orElseThrow(() -> new ResourceNotFoundException("Todo not found with id: " + id));
    }

    @Override
    public Todo save(Todo todo) {
        return todoRepository.save(todo);
    }

    @Override
    public void deleteById(String id) {
        Todo todo = findById(id);
        todoRepository.delete(todo);
    }
}
