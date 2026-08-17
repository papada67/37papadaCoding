<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ระบบติดตามงานนักเรียน</title>
    <!-- ใช้ Tailwind CSS ผ่าน CDN เพื่อความรวดเร็ว -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-slate-100 font-sans min-h-screen p-4 md:p-8">

    <div class="max-w-4xl mx-auto">
        <!-- Header -->
        <header class="bg-indigo-600 text-white p-6 rounded-t-xl shadow-lg flex justify-between items-center">
            <div>
                <h1 class="text-2xl font-bold"><i class="fa-solid fa-list-check mr-2"></i>ติดตามการส่งงานนักเรียน</h1>
                <p class="text-indigo-200 text-sm">จัดการและติดตามสถานะการส่งการบ้าน</p>
            </div>
            <button onclick="toggleModal()" class="bg-white text-indigo-600 px-4 py-2 rounded-lg font-semibold hover:bg-indigo-50 transition shadow">
                + สั่งงานใหม่
            </button>
        </header>

        <!-- Task List Section -->
        <main class="bg-white p-6 rounded-b-xl shadow-md">
            <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse">
                    <thead>
                        <tr class="border-b-2 border-slate-200 text-slate-600">
                            <th class="p-3">ชื่อวิชา / รายงาน</th>
                            <th class="p-3">ชื่อนักเรียน</th>
                            <th class="p-3">กำหนดส่ง</th>
                            <th class="p-3">สถานะ</th>
                            <th class="p-3 text-center">จัดการ</th>
                        </tr>
                    </thead>
                    <tbody id="taskList">
                        <!-- รายการงานจะถูกเพิ่มที่นี่ผ่าน JavaScript -->
                    </tbody>
                </table>
            </div>
        </main>
    </div>

    <!-- Modal สำหรับเพิ่มงานใหม่ -->
    <div id="taskModal" class="fixed inset-0 bg-black bg-opacity-50 hidden flex items-center justify-center p-4">
        <div class="bg-white rounded-xl p-6 w-full max-w-md shadow-2xl">
            <h2 class="text-xl font-bold text-slate-800 mb-4">เพิ่มการมอบหมายงาน</h2>
            <form id="taskForm" onsubmit="addTask(event)">
                <div class="mb-3">
                    <label class="block text-sm font-medium text-slate-600 mb-1">ชื่อวิชา / ชื่องาน</label>
                    <input type="text" id="subject" required class="w-full border p-2 rounded-md focus:outline-indigo-500">
                </div>
                <div class="mb-3">
                    <label class="block text-sm font-medium text-slate-600 mb-1">ชื่อนักเรียน</label>
                    <input type="text" id="student" required class="w-full border p-2 rounded-md focus:outline-indigo-500">
                </div>
                <div class="mb-4">
                    <label class="block text-sm font-medium text-slate-600 mb-1">กำหนดส่ง</label>
                    <input type="date" id="dueDate" required class="w-full border p-2 rounded-md focus:outline-indigo-500">
                </div>
                <div class="flex justify-end gap-2">
                    <button type="button" onclick="toggleModal()" class="px-4 py-2 text-slate-500 hover:bg-slate-100 rounded-md">ยกเลิก</button>
                    <button type="submit" class="px-4 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700">บันทึก</button>
                </div>
            </form>
        </div>
    </div>

    <script>
        // ข้อมูลตัวอย่าง
        let tasks = [
            { id: 1, subject: 'คณิตศาสตร์ (แบบฝึกหัดที่ 3)', student: 'สมชาย ใจดี', dueDate: '2026-08-20', status: 'ส่งแล้ว' },
            { id: 2, subject: 'ภาษาไทย (เรียงความ)', student: 'สมหญิง รักเรียน', dueDate: '2026-08-18', status: 'ยังไม่ส่ง' }
        ];

        function renderTasks() {
            const list = document.getElementById('taskList');
            list.innerHTML = '';
            
            tasks.forEach(t => {
                const isDone = t.status === 'ส่งแล้ว';
                const row = document.createElement('tr');
                row.className = 'border-b border-slate-100 hover:bg-slate-50';
                row.innerHTML = `
                    <td class="p-3 font-medium text-slate-800">${t.subject}</td>
                    <td class="p-3 text-slate-600">${t.student}</td>
                    <td class="p-3 text-slate-500">${t.dueDate}</td>
                    <td class="p-3">
                        <span class="px-3 py-1 text-xs rounded-full ${isDone ? 'bg-green-100 text-green-700' : 'bg-amber-100 text-amber-700'}">
                            ${t.status}
                        </span>
                    </td>
                    <td class="p-3 text-center">
                        <button onclick="toggleStatus(${t.id})" class="text-sm text-indigo-600 hover:underline mr-2">
                            ${isDone ? 'ทำเป็นยังไม่ส่ง' : 'ทำเป็นส่งแล้ว'}
                        </button>
                        <button onclick="deleteTask(${t.id})" class="text-sm text-red-500 hover:underline">ลบ</button>
                    </td>
                `;
                list.appendChild(row);
            });
        }

        function toggleModal() {
            document.getElementById('taskModal').classList.toggle('hidden');
        }

        function addTask(e) {
            e.preventDefault();
            const subject = document.getElementById('subject').value;
            const student = document.getElementById('student').value;
            const dueDate = document.getElementById('dueDate').value;

            tasks.push({ id: Date.now(), subject, student, dueDate, status: 'ยังไม่ส่ง' });
            renderTasks();
            toggleModal();
            document.getElementById('taskForm').reset();
        }

        function toggleStatus(id) {
            tasks = tasks.map(t => t.id === id ? { ...t, status: t.status === 'ส่งแล้ว' ? 'ยังไม่ส่ง' : 'ส่งแล้ว' } : t);
            renderTasks();
        }

        function deleteTask(id) {
            tasks = tasks.filter(t => t.id !== id);
            renderTasks();
        }

        // แสดงรายการครั้งแรก
        renderTasks();
    </script>
</body>
</html>