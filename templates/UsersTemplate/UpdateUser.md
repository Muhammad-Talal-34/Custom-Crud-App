{% extends 'base.html' %}
{% load static %}
{% block extra_css %}
    <link rel="stylesheet" href="{% static 'css/addUser.css' %}">
{% endblock %}

{% block content %}
<div class="crud-card form-card">
    <div class="crud-header form-header">
        <div>
            <h2>Add New User</h2>
            <p class="text-muted">Enter the details below to create a new user profile.</p>
        </div>
        
    </div>

    <!-- enctype is REQUIRED for uploading images in Django -->
    <form action="" method="POST" enctype="multipart/form-data" class="custom-form">
        {% csrf_token %}
        
        <!-- Grid Row for Name and Email -->
        <div class="form-row">
            <div class="form-group">
                <label for="id_u_name">Full Name <span class="required">*</span></label>
                <input type="text" id="id_u_name" name="name" value={{user.u_name}} maxlength="33" required placeholder="e.g. John Doe">
            </div>

            <div class="form-group">
                <label for="id_u_email">Email Address <span class="required">*</span></label>
                <input type="email" id="id_u_email" name="email" value={{user.u_email}} required placeholder="e.g. john@example.com">
            </div>
        </div>

        <div class="form-group w-50">
            <label for="id_u_age">Age <span class="required">*</span></label>
           
<input type="number" id="id_u_age" name="age" value="{{ user.u_age }}" min="0" required>
        </div>

        <!-- Styled Dropzone for File Upload -->
        <div class="form-group file-drop-area">
            <label for="id_u_image">Profile Image <span class="optional">(Optional)</span></label>
            <div class="dropzone-box">
                <input type="file" id="id_u_image" name="image" value="u_image" accept="image/*" class="file-input">
            </div>
        </div>

        <div class="form-actions">
            <button type="submit" class="btn-save">Save User</button>
            <a href="{% url 'users' %}" class="btn-cancel">Cancel</a>
           
        </div>
    </form>
</div>
{% endblock %}