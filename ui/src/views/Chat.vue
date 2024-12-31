<template>
    <img :src="GrainImg" alt="Grain image" class="absolute -z-10 top-0 left-0 opacity-40 w-screen h-screen">
    <router-link :to="{ name: 'home' }"> <img :src="UpArr"
            class="-rotate-90 w-3 cursor-pointer opacity-70 absolute left-4 top-3" alt="Left Arrow"></router-link>
    <main class="flex items-center justify-center h-screen">
        <section class="text-center" v-if="!first_question_was_asked">
            <h2 class="text-4xl">Start talking with yourself!</h2>
            <div class="flex mt-7 w-[500px] pr-5 items-center bg-[#26262e] rounded-md">
                <input class="h-12 w-full outline-none bg-transparent box-border px-4" placeholder="Send a Message"
                    type="text" v-model="question" @keyup.enter="sendQuestion">
                <img :src="DiagArr" alt="Send Icon" class="w-4 cursor-pointer opacity-85 relative h-4"
                    @click="sendQuestion">
            </div>
            <div class="mt-7">
                <span class="border-[#3f3f4a] border inline-flex gap-3 px-3 rounded-full items-center">
                    <img :src="HeartIcon" class="w-3.5 opacity-70 inline-block" alt="Heart icon">
                    <p class="text-[#757580] rounded-full inline py-1">Ask about your
                        interests</p>
                </span>
                <span class="border-[#3f3f4a] ml-3 border inline-flex gap-3 px-3 rounded-full items-center">
                    <img :src="BrainIcon" class="w-3.5 opacity-70 inline-block" alt="Heart icon">
                    <p class="text-[#757580] rounded-full inline py-1">Dive into your psyche</p>
                </span>
            </div>
        </section>
        <section class="w-full px-5 max-w-[700px] grid grid-rows-[12fr_1fr]" v-else>
            <section ref="conversation_window" class="overflow-auto pt-5 max-h-[85vh]">
                <div v-for="exchange in conversation" class="h-auto">
                    <p class="max-w-[600px] mt-10 text-right"> {{
                        exchange.question }}</p>
                    <div class="max-w-[600px]">
                        <img :src="DaylioAI" alt="DaylioPic" class="w-5">
                        <p class="mt-5 h-auto" v-html="formatResponse(exchange.response)"></p>
                    </div>
                </div>
            </section>
            <div class="flex mt-7 w-full pr-5 items-center bg-[#26262e] rounded-md">
                <input class="h-12 w-full outline-none bg-transparent box-border px-4" placeholder="Send a Message"
                    type="text" v-model="question" @keyup.enter="sendQuestion">
                <img :src="DiagArr" alt="Send Icon" class="w-4 cursor-pointer opacity-85 relative h-4"
                    @click="sendQuestion">
            </div>
        </section>
        <p class="absolute right-10 top-0 z-30 cursor-pointer hover:underline" @click="switchModes">{{ mode }} Mode
            Enabled
        </p>
    </main>
</template>

<script setup lang="ts">
import { marked } from "marked"
import BookIcon from "@/assets/book-icon.png"
import DiagArr from "@/assets/diag-arrow.png"
import StraightArr from "@/assets/straight-arr.png"
import UpArr from "@/assets/up-arrow.png"
import GrainImg from "@/assets/grain.png"
import BrainIcon from "@/assets/brain-icon.png"
import HeartIcon from "@/assets/heart-icon.png"
import DaylioAI from "@/assets/icon.png"
import { ref, nextTick } from "vue"
import axios from "axios"

type ConversationT = {
    question: string,
    response: string
}

type ModesT = "RAG" | "Full-Context"

const mode = ref<ModesT>("RAG")
const question = ref<string>("")
const first_question_was_asked = ref<boolean>(false)
const waiting_for_response = ref<boolean>(false)
const conversation = ref<ConversationT[]>([])
const conversation_window = ref<HTMLElement>()
let conversation_index = 0

function scrollToBottom() {
    const div = conversation_window.value;
    if (div) {
        div.scrollTop = div.scrollHeight;
    }
}

async function sendQuestion() {
    try {
        if (question.value.trim() === "") {
            // This is just for now [for ease]
            alert("Please enter a message")
            return
        }

        first_question_was_asked.value = true
        waiting_for_response.value = true

        conversation.value.push({
            question: question.value,
            response: "..."
        })

        nextTick(() => {
            scrollToBottom()
        })

        let question_saved = question.value
        question.value = "" //So that I can clear the input field

        let res = await axios.post("http://localhost:5000/ask", {
            question: question_saved,
            mode: mode.value
        })

        conversation.value[conversation_index].response = res.data
        waiting_for_response.value = false

        conversation_index++

        nextTick(() => {
            scrollToBottom()
        })
        console.log(res)
    } catch (err) {
        console.log(err)
    }
}

function formatResponse(response: string) {
    return "<p>" + marked.parse(response.replace(/\n/g, "<br>")) + "</p>";
}

function switchModes() {
    mode.value = mode.value === "RAG" ? "Full-Context" : "RAG"
}
</script>