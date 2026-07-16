# AI Student Support Assistant 互动式教案草案

## 1. 课程定位

本课程不是让学生从零开发一个完整管理系统，而是基于一个真实教育管理系统的简化场景，带学生完成一个可实操的 AI 项目闭环。

项目主线：

```text
Real School Operation
→ Data Collection
→ Structured Database
→ Python Analysis
→ AI Summary
→ Student Learning Profile
→ Human Review
```

课程最终项目名称：

```text
AI Student Support Assistant
```

两个核心模块：

```text
Module 1: Summer Camp Sign-in/out Data Collection
训练：Web + API + Database + CSV

Module 2: Student Learning Profile
训练：Python Analysis + AI Comment Summary + Dashboard
```

## 2. 学生对象

适合对象：

- 高中生
- 多数学生有 Python 基础
- Excel/CSV 可以接受
- HTML 基础较弱或没有
- 无完整系统项目经验也可以参加
- 对 AI、数据、Web 项目感兴趣
- 适合 4 人一组完成

预期基础：

- 不要求会完整开发网站
- 不要求会机器学习
- 可以使用 Python 基础语法
- 可以阅读和编辑 CSV/Excel
- 最好能理解基础英文技术词汇
- 会使用浏览器、Excel/CSV、简单复制粘贴代码即可开始

项目背景：

- 本次以比赛项目为目标
- 后续可以延展为正式课程
- 可以接入 OpenAI API
- 使用脱敏数据或 demo 数据
- 学习材料以英文为主，中文作为辅助说明

## 3. 课程形式

建议做成一个互动式自学网站，每个 lesson 都像任务卡。

学习方式：

- 总周期：4 周
- 学生主要在家自学
- 每周至少完成 2 个 lesson
- 每个 lesson 都有学习内容、练习、提交物和检查点
- 课堂或线上讨论用于答疑、阶段检查和项目整合

网站结构：

```text
Home
Week 1: From Real Operation to Data
Week 2: API, Database, and Python Analysis
Week 3: AI Comment Summary and Student Learning Profile
Week 4: Dashboard, Responsible AI, and Final Presentation
Resources
Templates
FAQ
Final Project
```

每个 lesson 页面统一结构：

```text
Goal
Why it matters
Key concepts
Step-by-step activity
Example
Your task
Check your work
Extension
Submit
```

## 4. 课程总目标

学生完成课程后应该能解释：

- 什么是真实业务问题
- 真实行为如何变成数据
- 为什么 AI 项目需要结构化数据
- API 如何连接网页和数据
- CSV 和数据库分别有什么作用
- Python 如何做基础分析
- AI 如何总结老师评论
- Dashboard 如何展示 AI 结果
- 为什么 AI 建议需要人工审核
- 为什么学生数据需要隐私保护

## 5. 最终交付物

每组最终提交：

- 一个 sign-in/out demo 或流程演示
- 一份 attendance CSV
- 一份 teacher comments CSV
- 一个 Python analysis notebook
- 一个 AI comment summary 示例
- 一个 Student Learning Profile dashboard 或 demo website
- 一份 Responsible AI statement
- 一个 5-8 页英文 final presentation
- 一个 3 分钟 demo

### Website 和 Dashboard 的区别

在本项目中，可以这样理解：

- Website：整个自学课程网站或项目展示网站，包含项目介绍、学习内容、资料下载、lesson 页面、最终作品说明。
- Dashboard：项目最终 demo 的一个功能页面，用来展示学生画像、出勤分析、AI summary 和学习支持建议。

简单说：

```text
Website = 学习和展示的整体入口
Dashboard = 项目成果中的数据展示页面
```

对学生来说，不要求从零开发复杂网站。可以提供模板，让他们主要完成 dashboard 内容和最终展示。

## 6. 四人分工

### Student 1: Data Collection & API

负责：

- 理解 sign-in/out 流程
- 测试 search / sign-in / sign-out API
- 理解 request / response
- 解释 JSON 数据

产出：

- API 测试截图或记录
- 一份 API response 说明

### Student 2: Database & CSV

负责：

- 设计 attendance CSV
- 理解数据库字段
- 整理导出的签到数据
- 检查数据是否干净

产出：

- attendance.csv
- 数据字段说明表

### Student 3: Python + AI Summary

负责：

- 用 Python 读取 CSV
- 计算出勤率、缺勤次数
- 读取老师 comments
- 用 AI 总结 comment

产出：

- Python notebook
- AI summary JSON

### Student 4: Dashboard + Presentation

负责：

- 设计 Student Learning Profile 页面
- 展示 attendance summary
- 展示 AI comment summary
- 整理最终汇报

产出：

- Dashboard 原型
- Final presentation

## 7. Week 1: From Real Operation to Data

### Lesson 1: What Problem Are We Solving?

Goal:

理解项目不是为了“炫技”，而是解决真实教育管理问题。

Why it matters:

AI 项目必须从真实问题开始。如果没有真实业务场景，AI 不知道该解决什么。

Key concepts:

- Real school operation
- Attendance
- Sign-in / sign-out
- Student support
- Human review

Activity:

学生阅读一个简单场景：

```text
A student arrives at summer camp.
The front desk searches the student's name.
The system shows the classroom.
The student signs in.
At the end of the day, the student signs out.
The school exports attendance data.
Later, the data is used to understand student support needs.
```

Your task:

画出流程图：

```text
Student arrives
→ Search student
→ Show classroom
→ Sign in
→ Record time
→ Sign out
→ Export attendance data
```

Check your work:

- 是否包含 sign in
- 是否包含 sign out
- 是否包含 attendance record
- 是否包含后续分析

Extension:

讨论如果没有签到数据，AI 是否能分析学生出勤情况。

### Lesson 2: What Data Should We Collect?

Goal:

理解真实行为如何变成数据字段。

Key concepts:

- Row
- Column
- Field
- Record
- student_id

Activity:

学生观察一个签到记录：

```text
Emma Chen came to camp on July 6.
She was assigned to Room 2.
She signed in at 9:04 AM.
She signed out at 4:02 PM.
```

Your task:

把这句话拆成字段：

```text
student_name: Emma Chen
date: 2026-07-06
room: Room 2
sign_in_time: 09:04
sign_out_time: 16:02
status: signed_out
```

产出：

设计 `attendance.csv` 字段：

```text
attendance_id
student_id
student_name
date
room
sign_in_time
sign_out_time
status
```

### Lesson 3: Try the Sign-in/out Demo

Goal:

体验数据采集模块。

Key concepts:

- Web form
- Button
- System feedback
- CSV export

Activity:

学生使用现成 demo：

1. 输入 first name
2. 输入 last name
3. 点击 Search
4. 查看 classroom
5. 点击 Sign In
6. 点击 Sign Out
7. 查看导出的 CSV

Your task:

记录一次完整操作：

```text
Student:
Room:
Sign-in time:
Sign-out time:
Final status:
```

Check your work:

- 是否能找到学生
- 是否能看到 room
- 是否生成 attendance record
- 是否能导出 CSV

## 8. Week 2: API, Database, and Python Analysis

### Lesson 4: What Is an API?

Goal:

理解网页和系统之间如何传递数据。

Key concepts:

- API
- Request
- Response
- JSON
- Endpoint

Example:

```text
GET /api/checkin/search?first_name=Emma&last_name=Chen
```

Response:

```json
{
  "student_id": 101,
  "student_name": "Emma Chen",
  "room": "Room 2",
  "status": "not_arrived"
}
```

Your task:

标注 JSON 中每个字段的含义：

```text
student_id:
student_name:
room:
status:
```

Check your work:

- 是否能解释 request 是什么
- 是否能解释 response 是什么
- 是否能指出 JSON 中的 key 和 value

### Lesson 5: From CSV to Database

Goal:

理解 CSV 和数据库的关系。

Key concepts:

- CSV
- Database
- Table
- Primary key
- Foreign key

Activity:

对比：

```text
CSV: Easy to open and share
Database: Better for storing, searching, and connecting data
```

Your task:

解释为什么 `student_id` 比 `student_name` 更适合连接数据。

Mini exercise:

```sql
SELECT student_id, COUNT(*) AS attendance_count
FROM attendance
GROUP BY student_id;
```

产出：

3 条 SQL 查询：

- 查询某个学生的签到记录
- 统计每个学生签到次数
- 统计每天总签到人数

### Lesson 6: Python Reads Attendance Data

Goal:

用 Python 分析 CSV。

Key concepts:

- Python
- pandas
- DataFrame
- count
- rate

Starter code:

```python
import pandas as pd

df = pd.read_csv("attendance.csv")
print(df.head())
```

Activity:

计算：

```python
total_records = len(df)
signed_in = len(df[df["status"] == "signed_in"])
signed_out = len(df[df["status"] == "signed_out"])
absent = len(df[df["status"] == "absent"])
```

Your task:

输出：

```text
Total records:
Signed in:
Signed out:
Absent:
Absence rate:
```

产出：

- 一个 notebook
- 一个简单统计结果
- 一张 bar chart

## 9. Week 3: AI Comment Summary and Student Learning Profile

### Lesson 7: Structured Data vs Teacher Comments

Goal:

理解为什么老师 comments 适合用 AI 处理。

Key concepts:

- Structured data
- Unstructured text
- Teacher comment
- Learning evidence

Example comments:

```text
Student understands loops but needs more practice with debugging.
Student participates well and completed the project independently.
Student missed the last class and needs to review variables.
```

Your task:

手动提取：

```text
mastered:
needs_review:
next_step:
```

Check your work:

- 是否能找出学生掌握的内容
- 是否能找出需要复习的内容
- 是否能给出下一步建议

### Lesson 8: AI Prompt for Comment Summary

Goal:

学习如何让 AI 输出结构化 summary。

Key concepts:

- Prompt
- JSON output
- Parent-friendly summary
- Human review

Prompt template:

```text
You are helping a coding school summarize teacher comments.

Extract:
1. mastered skills
2. needs review
3. next step
4. parent-friendly summary

Return JSON.

Comment:
"Student understands loops but needs more practice with debugging."
```

Expected output:

```json
{
  "mastered": ["loops"],
  "needs_review": ["debugging"],
  "next_step": "Practice debugging before the next project.",
  "parent_summary": "The student is making progress but needs more practice with debugging."
}
```

Your task:

用 3 条老师 comment 生成 3 个 AI summaries。

Check your work:

- AI 是否输出 JSON
- 是否有 mastered
- 是否有 needs_review
- 是否有 parent_summary
- 输出是否友好、谨慎

### Lesson 9: Build a Student Learning Profile

Goal:

把 attendance、comments 和 AI summary 合成学生画像。

Key concepts:

- Profile
- Attendance summary
- Makeup status
- Learning tags
- Support suggestion

Profile template:

```text
Student Name:
Current Course:
Attendance Summary:
Makeup Status:
Strengths:
Needs Review:
Next Step:
Parent-Friendly Summary:
Human Review:
```

Your task:

为一个学生生成完整 profile。

Example:

```text
Student: Emma Chen
Attendance: 8/10 attended
Makeup: 1 pending
Strengths: loops, participation
Needs Review: debugging
Next Step: Complete debugging practice
Human Review: Teacher should confirm before sharing with parent
```

## 10. Week 4: Dashboard, Responsible AI, and Final Presentation

### Lesson 10: Build a Simple Dashboard

Goal:

把分析结果变成别人能看懂的页面。

Recommended tool:

```text
Streamlit
```

Why Streamlit:

- 适合 Python 初学者
- 不需要复杂前端
- 很快能做出 dashboard
- 学生已有 Python 基础，因此比从零学习 HTML/JavaScript 更合适

Starter layout:

```text
Student Learning Profile

Student Name
Course
Attendance Summary
Makeup Status
AI Comment Summary
Next Step
Responsible AI Notice
```

Your task:

做一个 dashboard 页面，至少显示：

- Student name
- Attendance rate
- AI summary
- Next step

### Lesson 11: Responsible AI

Goal:

理解 AI 输出不能直接替代老师判断。

Key concepts:

- Privacy
- Bias
- Human review
- Sensitive student data
- Parent-facing language

Rules:

- 不使用真实学生隐私数据
- 使用模拟或脱敏数据
- AI 只是建议
- 老师或管理员必须审核
- 不给学生贴负面标签
- 给家长看的语言必须友好、谨慎

Required statement:

```text
The AI assistant provides learning support suggestions, but final decisions should always be reviewed by teachers or administrators.
```

Your task:

写 3 条 responsible AI rules。

### Lesson 12: Final Presentation

Goal:

把项目讲清楚。

Presentation structure:

```text
1. Real problem
2. Data collection
3. Database / CSV
4. Python analysis
5. AI summary
6. Student Learning Profile
7. Human review
8. Responsible AI
```

Final demo flow:

```text
Search student
→ Sign in
→ Export attendance CSV
→ Analyze with Python
→ Summarize teacher comment with AI
→ Show Student Learning Profile
→ Explain human review
```

Your task:

准备：

- 5-8 页 slides
- 3 分钟 demo
- 每个组员讲 30-45 秒

## 11. 互动网站功能建议

网站可以包含：

- Lesson navigation
- Progress checklist
- Download templates
- Copy code buttons
- Practice data
- Mini quiz
- Submit checklist
- FAQ
- Final project rubric

### 建议网站页面

```text
Home
Project Story
4-Week Learning Path
Week 1 Lessons
Week 2 Lessons
Week 3 Lessons
Week 4 Lessons
Templates
API Examples
OpenAI Prompt Examples
Final Project Guide
Competition Presentation Guide
Responsible AI Checklist
FAQ
```

网站语言建议：

- 页面标题和核心术语使用英文
- 关键说明可以中英双语
- 学生最终 PPT 以英文为主
- 中文材料保留给教师和助教使用

### 每课页面组件

```text
Lesson title
Estimated time
Goal
Key vocabulary
Step-by-step task
Code/example block
Try it yourself
Check your work
Common mistakes
Extension challenge
Submit button/checklist
```

## 12. 资料包清单

需要准备：

### 数据资料

- students.csv
- attendance.csv
- teacher_comments.csv
- courses.csv
- makeup_lessons.csv

### 代码资料

- sign-in page template
- API response examples
- Python notebook template
- Streamlit dashboard template
- AI prompt template

### 教学资料

- project overview
- vocabulary sheet
- responsible AI checklist
- final presentation template
- grading rubric
- instructor guide

## 13. 评分 Rubric

建议 100 分：

```text
Problem understanding: 15
Data collection and structure: 15
API / CSV / database understanding: 15
Python analysis: 15
AI comment summary: 15
Dashboard and presentation: 15
Responsible AI: 10
```

## 14. 教师检查点

### Week 1 Checkpoint

- 学生能解释 sign-in/out 流程
- 学生完成 attendance 字段设计
- 学生完成一次 demo 操作

### Week 2 Checkpoint

- 学生能解释 API response
- 学生完成基础 SQL 或 CSV 查询
- 学生完成 Python 读取 CSV

### Week 3 Checkpoint

- 学生完成 AI comment summary
- 学生生成一个 Student Learning Profile

### Week 4 Checkpoint

- Dashboard 可展示
- Responsible AI statement 完成
- Final presentation 完成

## 15. 需要进一步确认的问题

为了做成正式课程包，还需要确认：

1. 学生具体年级
2. 每周是否有固定线上/线下答疑时间
3. 每次答疑或 workshop 多长时间
4. 比赛提交格式要求
5. 是否需要项目视频
6. OpenAI API key 由谁提供
7. 是否需要统一开发环境
8. 是否需要把 dashboard 部署到网上
9. 学校是否希望后续扩展为正式课程
10. 是否需要家长或学校层面的数据使用说明

## 16. 当前已确认设定

```text
学生基础：多数人学过 Python 基础，Excel 可以，HTML 基础较弱或没有
课程周期：4 周
学习方式：在家自学为主，每周至少 2 课
AI 工具：可以接 OpenAI API
项目用途：本次用于比赛，后续可能延展为课程
语言：英文为主，中文辅助
最终形式：PPT 讲解 + demo website/dashboard
数据：使用脱敏数据或 demo 数据
```
