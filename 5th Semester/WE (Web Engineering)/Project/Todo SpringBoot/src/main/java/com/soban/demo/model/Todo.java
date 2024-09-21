package com.soban.demo.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import lombok.Data;

@Data
@Document(collection = "todos")
public class Todo {
    @Id
    private String id;
    private String title;
    private String description;
    private boolean completed;
}
