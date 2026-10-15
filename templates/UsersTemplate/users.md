{% extends 'base.html' %}
{% load static %}
{% block extra_css %}
    <link rel="stylesheet" href="{% static 'css/users.css' %}">
{% endblock %}
{% block content %}
<div class="crud-card">
    <div class="crud-header">
        <h2>User Management</h2>
        <!-- This button will eventually link to your Add User form -->
        <a href="/adduser" class="btn-add">+ Add New User</a> 
    </div>

    <div class="table-responsive">
        <table class="crud-table">
            <thead>
                <tr>
                    <th>Profile</th>
                    <th>Name</th>
                    <th>Email Address</th>
                    <th>Age</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {% for user in users %}
                <tr>
                    <td>
                        <!-- Django logic to check if an image exists -->
                        {% if user.u_image %}
                            <img src="{{ user.u_image.url }}" alt="{{ user.u_name }}" class="user-avatar">
                        {% else %}
                            <!-- Fallback if no image is uploaded (shows first letter of name) -->
                            <div class="avatar-placeholder">{{ user.u_name|make_list|first|upper }}</div>
                        {% endif %}
                    </td>
                    <td class="font-bold">{{ user.u_name }}</td>
                    <td>{{ user.u_email }}</td>
                    <td>{{ user.u_age }} yrs</td>
                    <td>
                        <a href="{% url 'updateuser' user.id %}" class="btn-action btn-edit">Edit</a>
                        <a href="{% url 'deleteuser' user.id %}" class="btn-action btn-delete">Delete</a>
                    </td>
                </tr>
                {% empty %}
                <tr>
                    <td colspan="5" class="empty-state">No users found in the database.</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>
{% endblock %}