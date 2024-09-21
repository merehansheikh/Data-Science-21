package com.soban.demo.service;

import java.util.List;
import com.soban.demo.model.Todo;

public interface TodoService {
    List<Todo> findAll();
    Todo findById(String id);
    Todo save(Todo todo);
    void deleteById(String id);
}
