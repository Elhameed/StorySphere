// // Function to open New Topic Modal
// function openNewTopicModal() {
//     // Code to open the modal for creating a new topic
//     var modal = document.getElementById('newTopicModal');
//     if (modal) {
//         modal.style.display = "block";
//         modal.addEventListener("click", function(event) {
//             if (event.target === modal) {
//                 closeModal('newTopicModal');
//             }
//         });
//     }
// }

// // Function to open Comments Modal
// function openCommentsModal() {
//     // Code to open the modal for viewing and adding comments
//     var modal = document.getElementById('commentsModal');
//     if (modal) {
//         modal.style.display = "block";
//         modal.addEventListener("click", function(event) {
//             if (event.target === modal) {
//                 closeModal('commentsModal');
//             }
//         });
//     }
// }

// // Function to open Reply Modal
// function openReplyModal() {
//     // Code to open the modal for replying to comments
//     var modal = document.getElementById('replyModal');
//     if (modal) {
//         modal.style.display = "block";
//         modal.addEventListener("click", function(event) {
//             if (event.target === modal) {
//                 closeModal('replyModal');
//             }
//         });
//     }
// }

// // Functions for interaction buttons (like, share, etc.)
// function likeTopic(topicId) {
//     // Get the CSRF token from the cookie
//     const csrfToken = getCookie('csrftoken');
    
//     // Code to handle liking a topic via AJAX
//     fetch(`/like-topic/${topicId}/`, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrfToken,
//         },
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.success) {
//             // Update the UI as needed
//             console.log('Topic liked successfully');
//         } else {
//             console.error('Failed to like the topic');
//         }
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// }

// function likeComment(commentId) {
//     // Get the CSRF token from the cookie
//     const csrfToken = getCookie('csrftoken');
    
//     // Code to handle liking a comment via AJAX
//     fetch(`/like-comment/${commentId}/`, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrfToken,
//         },
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.success) {
//             // Update the UI as needed
//             console.log('Comment liked successfully');
//         } else {
//             console.error('Failed to like the comment');
//         }
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// }


// function shareTopic() {
//     // Code to handle sharing a topic on social media
//     console.log('Share button clicked');
// }

// // Function to close modal
// function closeModal(modalId) {
//     var modal = document.getElementById(modalId);
//     if (modal) {
//         modal.style.display = "none";
//     }
// }

// // Function to get CSRF token for AJAX requests
// function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = cookies[i].trim();
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
