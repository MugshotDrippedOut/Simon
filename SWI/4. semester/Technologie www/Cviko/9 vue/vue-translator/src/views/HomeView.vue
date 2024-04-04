<script setup>
//import TheWelcome from '../components/TheWelcome.vue'
import { ref } from "vue";

const userInput = ref("");
const translationResult = ref("");

const translate = () => {
  console.log(userInput.value);
  const url = `https://api.mymemory.translated.net/get?q=${userInput.value}&langpair=en|cs`;
  if (!userInput.value || userInput.value.length < 2) {
    return;
  }
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      translationResult.value = data.responseData.translatedText;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};
</script>

<template>
  <main>
    <h1>Welcome to the Vue Translator</h1>
    <input
      v-model="userInput"
      type="text"
      placeholder="Text for translation..."
    />
    <button @click="translate">Translate</button>
    {{ userInput }} --> {{ translationResult }}


  </main>
</template>

<style scoped>

main {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

input {
  margin: 1rem;
  padding: 0.5rem;
  font-size: 1rem;
}



button {
  padding: 0.5rem 1rem;
  font-size: 1rem;
  background-color: var(--color-primary);
  color: white;
  border: none;
  cursor: pointer;
}
</style>