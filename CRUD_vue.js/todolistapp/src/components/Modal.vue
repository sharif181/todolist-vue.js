<template>
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
                        <input v-if= "isEdit" id="edit_input" type="text" :value= "task">
                        <p v-else> Do you want to delete {{this.todo}} ?</p>        
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                        <button v-if= "isEdit" v-on:click = 'execute_edit' value="" id='edit-id' type="button" class="btn btn-info" data-dismiss="modal">Update</button>
                        <button v-else v-on:click = 'execute_delete' value="" id='delete-id' type="button" class="btn btn-danger" data-dismiss="modal">Delete</button>
                    </div>
                    </div>
                </div>
            </div>
</template>


<script>
export default {
    name:'Modal',
    props:{
        isEdit : Boolean,
        task : String,
        todo : String,
        // delete_task:{
        //     type:Function
        // },
        // edit_task:{
        //     type:Function
        // }
    },

    methods:{
        execute_delete(){
            this.$emit('delete_task')
        },
        execute_edit(){
            this.$emit('edit_task')
        }
        // execute_delete(){
        //     this.delete_task()
        // },
        // execute_edit(){
        //     this.edit_task()
        // }
    }
    

}
</script>