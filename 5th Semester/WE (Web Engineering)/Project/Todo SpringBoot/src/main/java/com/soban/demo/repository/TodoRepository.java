package com.soban.demo.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import com.soban.demo.model.Todo;

public interface TodoRepository extends MongoRepository<Todo, String> {
}
