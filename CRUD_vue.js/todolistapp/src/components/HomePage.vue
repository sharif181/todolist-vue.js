<template>
    <div class="container mt-5">
        <div>
            <input v-on:keyup = "search_task" v-model= "search_text" name='search' type="text" placeholder="Search task">
            <button class="btn btn-success ml-3"> Search </button>
        </div>
        <div class="justify-content-between mt-2">
            <h5 class="display-5">Todo list app</h5>
        </div>
        <input  v-model= "task_text" name='task' type="text" class="form-control" placeholder="Add task..">
        <button v-on:click = "save_todo" type="submit" class="btn btn-primary mt-2">Save</button>
        <div class="card mt-2" v-for="todo in todos" :key="todo.id">
            <div class="card-body justify-content-between">
                <p>{{todo.task}} </p>
                <button v-on:click = "edit_task_helper(todo.id,todo.task)" class="btn btn-secondary m-2" :id="todo.id" data-toggle="modal" data-target="#exampleModal" data-whatever="@mdo"> Edit</button>
                <button v-on:click = "modal_show(todo.id,todo.task)" class="btn btn-danger" :id="todo.id" data-toggle="modal" data-target="#exampleModal"> Delete</button>
            </div>
        </div>
        <div id="modal">
           <Modal :isEdit= "isEdit" :task= "task" :todo= "todo" @delete_task = 'delete_task' @edit_task= "edit_task" />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Modal from './Modal.vue'

export default {
    name:'HomeView',
    components:{
        Modal
    },
    data(){
        return{
            todos: [],
            isEdit:false,
            task_text : "",
            search_text : "",
            task: "",
            todo: ""
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
            if(this.task_text.length>0){
                const todo = {task:this.task_text}
                axios.post('http://localhost:8000/',todo)
                .then(
                    res=> this.todos.unshift(res.data)
                )
                this.task_text = ""
                this.search_text = ""
            }else{
                alert('Insert at least on letter')
            }
        },
        search_task:function(){
            if(this.search_text.length==0) this.getValue()
            else{
                axios.get('http://localhost:8000/search/'+this.search_text)
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
            this.task = task
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
            this.todo = todo
        }
    },
    
}
</script>