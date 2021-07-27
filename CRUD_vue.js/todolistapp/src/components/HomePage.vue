<template>
    <div class="container mt-5">
        <div>
            <input v-on:keyup = "search_task"  name='search' type="text" placeholder="Search task">
            <button class="btn btn-success ml-3"> Search </button>
        </div>
        <div class="justify-content-between mt-2">
            <h5 class="display-5">Todo list app</h5>
        </div>
        <input name='task' type="text" class="form-control" placeholder="Add task..">
        <button v-on:click = "save_todo" type="submit" class="btn btn-primary mt-2">Save</button>
        <div class="card mt-2" v-for="todo in todos" :key="todo.id">
            <div class="card-body justify-content-between">
                <p>{{todo.task}} </p>
                <button v-on:click = "edit_task_helper(todo.id,todo.task)" class="btn btn-secondary m-2" :id="todo.id" data-toggle="modal" data-target="#exampleModal" data-whatever="@mdo"> Edit</button>
                <button v-on:click = "modal_show(todo.id,todo.task)" class="btn btn-danger" :id="todo.id" data-toggle="modal" data-target="#exampleModal"> Delete</button>
            </div>
        </div>
        <div id="delete_modal_div">
            <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                    <div class="modal-header">
                        <h5 v-if= "isEdit" class="modal-title" id="exampleModalLabel">Edit Task</h5>
                        <h5 v-else class="modal-title" id="exampleModalLabel">Delete Task</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                        <button v-if= "isEdit" v-on:click = 'edit_task()' value="" id='edit-id' type="button" class="btn btn-info" data-dismiss="modal">Update</button>
                        <button v-else v-on:click = 'delete_task()' value="" id='delete-id' type="button" class="btn btn-danger" data-dismiss="modal">Delete</button>
                    </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'


export default {
    name:'HomeView',
    data(){
        return{
            todos: [],
            isEdit:false
        }
    },
    mounted(){
        this.getValue()
    },
    
    methods:{
        async delete_task(){
            let btn = document.querySelector('#delete-id')
            let task_id = parseInt(btn.value)
            await axios.delete('http://localhost:8000/todo/'+task_id)
            .then()
            await this.getValue()
        },
        save_todo:function(){
            const task = document.querySelector("input[name=task]").value
            if(task.length>0){
                const todo = {task:task}
                axios.post('http://localhost:8000/',todo)
                .then(
                    res=> this.todos.unshift(res.data)
                )
                document.querySelector("input[name=task]").value = ""
                document.querySelector("input[name=search]").value = ""
            }else{
                alert('Insert at least on letter')
            }
        },
        search_task:function(){
            const task = document.querySelector("input[name=search]").value
            if(task.length==0) this.getValue()
            else{
                axios.get('http://localhost:8000/search/'+task)
                .then(res=>this.todos=res.data)
            }
        },

        async toggleButton(val){
            this.isEdit = val
        },

        async edit_task_helper(task_id,task){
            await this.toggleButton(true)
            var btn = document.querySelector('#edit-id')
            btn.value = task_id
            var input = document.querySelector('.modal-body')
            input.innerHTML = `<input id="edit_input" type="text" value="${task}">`
        },
        async edit_task(){
            var id = document.querySelector('#edit-id').value
            var task = document.querySelector('#edit_input').value
            let todo = {
                id:id,
                task:task
            }
            await axios.put('http://localhost:8000/todo/'+id,todo)
            .then()
            await this.getValue()
        },
        async getValue(){
            axios.get('http://localhost:8000/')
            .then(res => this.todos = res.data)
        },
        async modal_show(task_id,todo){
            await this.toggleButton(false)
            var btn = document.querySelector('#delete-id')
            btn.value = task_id
            document.querySelector('.modal-body').innerHTML =  `Do you want to delete `+todo+`?`
        }
    },
    
}
</script>