<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
    <main>
        <div class="flex-container">
            <img src="../assets/starshinelogo.png" class="image-placeholder" />
            <div class="welcome-message">
                good morning starshine... the earth says hello!
            </div>
            <div class="button-container">
                <button>log in</button>
                <button>sign up</button>
            </div>
        </div>
        <RouterLink class="guest-link" to="/alarm-list">continue as guest ></RouterLink>
    </main>
</template>

<style scoped>
    main {
        height: 80%;
        width: 80%;
        background-color: #ffe2f5;
        border-radius: 20px;
        opacity: 80%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0px 30px 30px rgba(0, 0, 0, 0.5);
    }

    .flex-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 6%;
    }

    .image-placeholder {
        margin-bottom: 2%;
    }

    .welcome-message {
        font-family: "Gloria Hallelujah", cursive;
        font-size: xx-large;
        color: #5b5b5b;
        margin-bottom: 2%;
        text-align: center;
    }

    .guest-link {
        align-self: flex-end;
        font-size: larger;
        text-decoration: none;
        color: #7b7b7b;
        margin-bottom: 3%;
        margin-right: 4%;
    }

    .button-container {
        /* border: 1px solid black; */
        width: 75%;
        display: flex;
        justify-content: center;
    }

    button {
        margin-left: 4%;
        margin-right: 4%;
        padding-top: 3%;
        padding-bottom: 3%;
        background-color: #ffc7c7;
        height: 100%;
        width: 80%;
        border: none;
        border-radius: 15px;
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        font-family: "Ubuntu Mono", monospace;
        font-size: xx-large;
    }
</style>