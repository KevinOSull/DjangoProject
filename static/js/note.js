const editButtons = document.querySelectorAll(".btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

for (let button of editButtons) {
    button.addEventListener("click", () => {
        let commentId = button.dataset.commentId;
        let commentContent = document.getElementById(`comment${commentId}`).innerText;

        commentText.value = commentContent;

        submitButton.innerText = "Update";

        commentForm.action = `/${button.dataset.slug}/edit_comment/${commentId}/`;
    });
}

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = button.dataset.commentId; 
        let slug = button.dataset.slug;
        // Set the delete link for the confirmation modal
        deleteConfirm.href = `/${slug}/delete_comment/${commentId}/`;
        deleteModal.show();
    });
}



