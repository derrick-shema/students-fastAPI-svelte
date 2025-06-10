<script lang="ts">
    import {onMount} from 'svelte';
    type Student = { id: number; first_name: string; last_name: string };
    let students: Student[] = [];

    onMount(async () => {
        const res = await fetch('http://localhost:8000');
        students = await res.json();
    })
</script>

<h2>Students</h2>
<ul>
    {#each students as student }
        <li>{student.first_name} {student.last_name}</li>
    {/each}
</ul>