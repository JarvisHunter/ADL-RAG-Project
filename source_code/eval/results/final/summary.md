# Evaluation results

Generated 2026-11-14 23:50

## Summary

| Model | Questions | Retrieval hit rate | Mean keyword score | Out-of-scope refusals | Answerable but refused | Mean latency (s) |
|---|---|---|---|---|---|---|
| qwen3.5:0.8b | 27 | 96% | 0.80 | 4/4 | 2/23 | 8.9 |
| hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 | 27 | 96% | 0.62 | 2/4 | 0/23 | 6.1 |
| llama3.2:3b | 27 | 96% | 0.86 | 4/4 | 2/23 | 9.1 |
| qwen2.5:3b | 27 | 96% | 0.75 | 4/4 | 5/23 | 6.8 |
| gemma3:4b | 27 | 96% | 0.89 | 4/4 | 1/23 | 10.5 |
| qwen3.5:9b | 27 | 96% | 0.87 | 4/4 | 2/23 | 16.3 |

## Answers

### Q01 · qwen3.5:0.8b · program_requirements
**Q:** How many credits are required for the Computer Science major?

**Reference:** The major requires 56 credits.

**Answer:** The Computer Science major requires 56 credits in total, which includes 40 credits in General Curriculum Requirements and 16 credits in Major Requirements.

[CS_MajorHandbook.pdf p.2]

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.86); CS_MajorHandbook.pdf p.7 (0.80); CS_MajorHandbook.pdf p.2 (0.76); CS_MajorHandbook.pdf p.13 (0.76); CS_MajorHandbook.pdf p.4 (0.74)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 9.64s

### Q02 · qwen3.5:0.8b · program_requirements
**Q:** Which courses are required for the Computer Science major?

**Reference:** CS 101, CS 201, CS 203, MATH 202, three intermediate courses, CS 302, four advanced courses, and Capstone I & II (or two additional intermediate/advanced courses).

**Answer:** The Computer Science major requires at least two Computer Science courses (MATH 202 - Discrete Math is also counted) and a total of six courses for the minor, including one programming course, a 100/200-level course, Data Structures & Algorithms, an intermediate course, and a 200/300-level course. Additionally, students must complete Military Training, Physical Education, and Political Courses.

[CS_MajorHandbook.pdf p.7]

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.82); CS_MajorHandbook.pdf p.7 (0.78); CS_MajorHandbook.pdf p.8 (0.75); CS_MajorHandbook.pdf p.14 (0.75); CS_MajorHandbook.pdf p.4 (0.75)  
*Retrieval hit:* True · *keyword score:* 0.17 · *latency:* 9.64s

### Q03 · qwen3.5:0.8b · academic_policies
**Q:** What must a student complete before formally declaring Computer Science as their major?

**Reference:** At least two Computer Science courses (MATH 202 Discrete Math also counts).

**Answer:** To formally declare Computer Science as their major, a student must complete at least two Computer Science courses (MATH 202 - Discrete Math is also counted). Additionally, the student must complete a minor in Computer Science by taking six courses, including one programming course (CS 101, CS 103, or CS 104), one 100-level or 200-level CS course, CS 201 (Data Structures & Algorithms), one intermediate course, one 200-level or 300-level CS course, and one advanced course.
[CS_MajorHandbook.pdf p.7]

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.81); CS_MajorHandbook.pdf p.1 (0.71); CS_MajorHandbook.pdf p.4 (0.70); CS_MajorHandbook.pdf p.14 (0.70); CS_MajorHandbook.pdf p.8 (0.70)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 12.46s

### Q04 · qwen3.5:0.8b · program_requirements
**Q:** How many credits and courses does the Computer Science minor require?

**Reference:** 24 credits: six courses.

**Answer:** The Computer Science minor requires 24 credits in total, consisting of 6 courses. Specifically, it mandates one programming course (4 credits), one 100-level or 200-level CS course (4 credits), CS 201 (4 credits), one intermediate course (4 credits), one 200-level or 300-level CS course (4 credits), and one advanced course (4 credits). Additionally, the student must complete at least one Computer Science course (MATH 202 - Discrete Math is also counted).

[CS_MajorHandbook.pdf p.7]

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.88); CS_MajorHandbook.pdf p.7 (0.78); CS_MajorHandbook.pdf p.2 (0.76); CS_MajorHandbook.pdf p.13 (0.75); CS_MajorHandbook.pdf p.11 (0.75)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 10.3s

### Q05 · qwen3.5:0.8b · academic_policies
**Q:** What is required to declare a minor in Computer Science?

**Reference:** At least one Computer Science course (MATH 202 also counts).

**Answer:** To formally declare a minor in Computer Science, the student must complete at least one Computer Science course (MATH 202 - Discrete Math is also counted) and take a total of six courses: one programming course (4 credits), one 100-level or 200-level CS course (4 credits), CS 201 – Data Structures & Algorithms (4 credits), one intermediate course (4 credits), one 200-level or 300-level CS course (4 credits), and one advanced course (4 credits).

[CS_MajorHandbook.pdf p.7]

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.85); CS_MajorHandbook.pdf p.2 (0.69); CS_MajorHandbook.pdf p.1 (0.67); CS_MajorHandbook.pdf p.7 (0.65); CS_MajorHandbook.pdf p.11 (0.65)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 10.13s

### Q06 · qwen3.5:0.8b · academic_policies
**Q:** What are the eligibility criteria for enrolling in CS 401 Capstone I?

**Reference:** A minimum major GPA of 3.5 and approval of a successful application.

**Answer:** Eligibility criteria for enrollment in CS 401 Capstone I include a minimum major GPA of 3.5 and approval of a successful application.
[CS_MajorHandbook.pdf p.9]

*Retrieved:* CS_MajorHandbook.pdf p.9 (0.81); CS_MajorHandbook.pdf p.7 (0.63); CS_MajorHandbook.pdf p.8 (0.63); CS_MajorHandbook.pdf p.2 (0.62); CS_MajorHandbook.pdf p.13 (0.62)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 8.67s

### Q07 · qwen3.5:0.8b · academic_policies
**Q:** What can students do instead of the capstone, and what is the consequence?

**Reference:** Take two additional intermediate or advanced courses; they graduate without honors (capstone = graduate with honors).

**Answer:** Students can take the capstone as an alternative to the capstone, but it is not listed as a separate option in the provided context. The context does not specify consequences for taking the capstone instead of the capstone. I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.15 (0.61); CS_MajorHandbook.pdf p.12 (0.61); CS_MajorHandbook.pdf p.5 (0.59); CS_MajorHandbook.pdf p.4 (0.56); CS_MajorHandbook.pdf p.8 (0.56)  
*Retrieval hit:* True · *keyword score:* 0.0 · *latency:* 8.82s

### Q08 · qwen3.5:0.8b · course_offerings
**Q:** What are the prerequisites for CS 302 Algorithms & Theory of Computing?

**Reference:** CS 201 and MATH 202.

**Answer:** CS302 Algorithms & Theory of Computing requires the following prerequisites:
*   CS201 (Data Structures & Algorithms)
*   MATH 202 (Mathematics)

I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.17 (0.80); CS_MajorHandbook.pdf p.17 (0.74); CS_MajorHandbook.pdf p.14 (0.72); CS_MajorHandbook.pdf p.12 (0.71); CS_MajorHandbook.pdf p.13 (0.70)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 10.03s

### Q09 · qwen3.5:0.8b · course_offerings
**Q:** What is the prerequisite for CS311 Advanced Deep Learning?

**Reference:** CS313 Deep Learning for AI.

**Answer:** The prerequisite for CS311 Advanced Deep Learning is CS313 Deep Learning for Artificial Intelligence, as stated in the context.

[CS_MajorHandbook.pdf p.18]

*Retrieved:* CS_MajorHandbook.pdf p.18 (0.88); CS_MajorHandbook.pdf p.18 (0.80); CS_MajorHandbook.pdf p.18 (0.73); CS_MajorHandbook.pdf p.17 (0.71); CS_MajorHandbook.pdf p.13 (0.69)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 8.73s

### Q10 · qwen3.5:0.8b · course_offerings
**Q:** How often is CS 210 Computer Networks offered?

**Reference:** Its availability is listed as 'On holding' (not currently scheduled).

**Answer:** CS 210 Computer Networks is offered on a holding basis, meaning it is not offered every year but rather on a specific cycle or semester.

[CS_MajorHandbook.pdf p.16]

*Retrieved:* CS_MajorHandbook.pdf p.16 (0.75); CS_MajorHandbook.pdf p.13 (0.70); CS_MajorHandbook.pdf p.13 (0.66); CS_MajorHandbook.pdf p.17 (0.66); CS_MajorHandbook.pdf p.17 (0.63)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 8.28s

### Q11 · qwen3.5:0.8b · course_offerings
**Q:** Which programming language is mainly used in CS 201 Data Structures & Algorithms?

**Reference:** Java (with some Python/C++ implementations).

**Answer:** CS201: Data Structures & Algorithms uses Java as the main programming language.

[CS_MajorHandbook.pdf p.14]

*Retrieved:* CS_MajorHandbook.pdf p.14 (0.79); CS_MajorHandbook.pdf p.14 (0.75); CS_MajorHandbook.pdf p.16 (0.74); CS_MajorHandbook.pdf p.17 (0.71); CS_MajorHandbook.pdf p.11 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 7.65s

### Q12 · qwen3.5:0.8b · course_offerings
**Q:** What topics are covered in CS 211 Operating Systems?

**Reference:** Concurrency (processes, threads, scheduling, synchronization, deadlock), memory management (paging, segmentation, swapping), file systems, plus scalability, virtualization, security and distributed computing.

**Answer:** CS 211 Operating Systems covers the interface between user programs and hardware devices, including concurrency, processes, threads, CPU scheduling, context switching, synchronization, and deadlock. It also explores memory management issues like linking, allocation, and paging.

[CS_MajorHandbook.pdf p.16]

*Retrieved:* CS_MajorHandbook.pdf p.16 (0.79); CS_MajorHandbook.pdf p.16 (0.65); CS_MajorHandbook.pdf p.16 (0.65); CS_MajorHandbook.pdf p.14 (0.65); CS_MajorHandbook.pdf p.14 (0.64)  
*Retrieval hit:* True · *keyword score:* 0.67 · *latency:* 8.92s

### Q13 · qwen3.5:0.8b · course_offerings
**Q:** Give some examples of advanced courses in the Computer Science major.

**Reference:** Foundations of Software Engineering, Database Systems, Computer Security, Cloud Computing, HCI, Computer Graphics, Game Design, Machine Learning, Deep Learning, Advanced Deep Learning, Computer Vision, NLP, Optimization, Computational Social Media, Bioinformatics.

**Answer:** Based on the provided context, here are examples of advanced courses in the Computer Science major:

*   **Foundations of Software Engineering**
*   **Database Systems**
*   **Computer Security**
*   **Cloud Computing**
*   **Human-Computer Interaction**
*   **Computer Graphics**
*   **Game Design & Development**
*   **Machine Learning**
*   **Deep Learning**
*   **Advanced Deep Learning**
*   **Computer Vision**
*   **Natural Language Processing**
*   **Optimization**
*   **Computational Social Media**

These courses are listed under the "Advanced Courses" section in the provided documents.

*Retrieved:* CS_MajorHandbook.pdf p.8 (0.81); CS_MajorHandbook.pdf p.11 (0.78); CS_MajorHandbook.pdf p.7 (0.77); CS_MajorHandbook.pdf p.8 (0.76); CS_MajorHandbook.pdf p.8 (0.74)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 10.56s

### Q14 · qwen3.5:0.8b · course_offerings
**Q:** In CS 207 Software Construction, what kind of applications do students build?

**Reference:** Android applications using Java.

**Answer:** Students in CS 207 Software Construction build Android applications using Java. They also work in teams to practice designing software using UML models such as use-case, sequence, and class diagrams.

*Retrieved:* CS_MajorHandbook.pdf p.15 (0.76); CS_MajorHandbook.pdf p.16 (0.72); CS_MajorHandbook.pdf p.15 (0.70); CS_MajorHandbook.pdf p.11 (0.69); CS_MajorHandbook.pdf p.14 (0.68)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 8.18s

### Q15 · qwen3.5:0.8b · learning_outcomes
**Q:** What are the Major Learning Outcomes (MLOs) of the Computer Science program?

**Reference:** MLO1: understand fundamental CS (theory and systems); MLO2: explain emerging aspects of CS (AI, ML, data science...); MLO3: develop real-world applications.

**Answer:** The Major Learning Outcomes (MLOs) of the Computer Science program are listed in the document as MLO 1, MLO 2, and MLO 3.

*   MLO 1: Demonstrate an understanding of fundamental computer science by illustrating core concepts, comparing methods, analyzing and solving problems in both theory and systems.
*   MLO 2: Explain emerging aspects of the computer science discipline (e.g., artificial intelligence, machine learning, data science, business analytics, digital media, etc.).
*   MLO 3: Develop real-world applications (e.g., software systems and frameworks, mobile apps, data pipeline, etc.) by using knowledge of computer science and other disciplines.

*Retrieved:* CS_MajorHandbook.pdf p.5 (0.76); CS_MajorHandbook.pdf p.11 (0.73); CS_MajorHandbook.pdf p.4 (0.71); CS_MajorHandbook.pdf p.2 (0.70); CS_MajorHandbook.pdf p.4 (0.69)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 14.73s

### Q16 · qwen3.5:0.8b · learning_outcomes
**Q:** What are the Program Educational Objectives (PEOs)?

**Reference:** PEO1: skills for employment or graduate school; PEO2: professional/personal ethics, collaboration and communication; PEO3: become innovators and thinkers solving CS challenges.

**Answer:** The Program Educational Objectives (PEOs) for the Computer Science major include equipping students with necessary skills and knowledge to gain employment in industry or graduate school, inquiring into emerging aspects of the discipline, and cultivating students to become innovators and thinkers to solve computer science-related challenges.

*Retrieved:* CS_MajorHandbook.pdf p.4 (0.80); CS_MajorHandbook.pdf p.4 (0.62); CS_MajorHandbook.pdf p.4 (0.59); CS_MajorHandbook.pdf p.11 (0.59); CS_MajorHandbook.pdf p.4 (0.57)  
*Retrieval hit:* True · *keyword score:* 0.67 · *latency:* 8.16s

### Q17 · qwen3.5:0.8b · career
**Q:** What jobs have Computer Science graduates obtained?

**Reference:** Software engineer, testing engineer, AI engineer, data engineer, business analyst, product owner, product development manager.

**Answer:** Computer Science graduates have successfully gained employment as software engineers, testing engineers, AI engineers, data engineers, business analysts, and product development managers.

*Retrieved:* CS_MajorHandbook.pdf p.6 (0.71); CS_MajorHandbook.pdf p.5 (0.70); CS_MajorHandbook.pdf p.2 (0.64); CS_MajorHandbook.pdf p.4 (0.63); CS_MajorHandbook.pdf p.14 (0.62)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 8.51s

### Q18 · qwen3.5:0.8b · teaching_assessment
**Q:** How are students taught and assessed in the Computer Science major?

**Reference:** Active and collaborative learning; continuous formative assessment through discussion, in-class activities and applied learning, plus quizzes, exams, projects, presentations and the capstone.

**Answer:** Students are taught through active and collaborative learning methods, including lectures, labs, group discussions, and in-class activities. Assessment includes summative methods such as quizzes, exams, and group presentations, as well as formative assessment through discussion and programming tests.

[CS_MajorHandbook.pdf p.12]

*Retrieved:* CS_MajorHandbook.pdf p.12 (0.77); CS_MajorHandbook.pdf p.12 (0.74); CS_MajorHandbook.pdf p.4 (0.73); CS_MajorHandbook.pdf p.4 (0.72); CS_MajorHandbook.pdf p.14 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 13.25s

### Q19 · qwen3.5:0.8b · program_requirements
**Q:** How many exploratory courses must students take, and how many can count toward the major?

**Reference:** 6 exploratory courses (24 credits); up to 2 courses (8 credits) can count toward the major.

**Answer:** Students must take 6 exploratory courses, with up to 2 of them (8 credits) being eligible to count toward the major.
[CS_MajorHandbook.pdf p.7]

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.76); CS_MajorHandbook.pdf p.7 (0.68); CS_MajorHandbook.pdf p.6 (0.67); CS_MajorHandbook.pdf p.13 (0.64); CS_MajorHandbook.pdf p.11 (0.63)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 8.94s

### Q20 · qwen3.5:0.8b · ambiguous
**Q:** What degree is awarded after completing the degree requirements?

**Reference:** A B.S. in Computer Science. Note: the handbook's Degree Requirements section says 'Bachelor of Science in Applied Mathematics', an apparent copy-paste error that may mislead the model.

**Answer:** A Bachelor of Science in Applied Mathematics is awarded following the successful completion of the degree requirements.

*Retrieved:* CS_MajorHandbook.pdf p.6 (0.66); CS_MajorHandbook.pdf p.2 (0.62); CS_MajorHandbook.pdf p.3 (0.61); CS_MajorHandbook.pdf p.6 (0.60); CS_MajorHandbook.pdf p.5 (0.59)  
*Retrieval hit:* True · *keyword score:* 0.0 · *latency:* 8.11s

### Q21 · qwen3.5:0.8b · out_of_scope
**Q:** What is the tuition fee for the Computer Science program?

**Reference:** Not stated in the handbook; the chatbot should say it cannot find the information.

**Answer:** I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.2 (0.68); CS_MajorHandbook.pdf p.4 (0.65); CS_MajorHandbook.pdf p.19 (0.64); CS_MajorHandbook.pdf p.14 (0.64); CS_MajorHandbook.pdf p.4 (0.64)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 8.28s

### Q22 · qwen3.5:0.8b · other
**Q:** Which universities' programs were used as references for the CS curriculum?

**Reference:** Stanford University, Carnegie Mellon University and Cornell University.

**Answer:** The documents provided reference several universities' programs as references for the CS curriculum. Specifically, the **CS_MajorHandbook.pdf** indicates that Computer Science students have successfully applied to graduate programs in the **United States and Europe**, including:

*   MSc/PhD Computer Science
*   MSc Data Science
*   MSc Bioinformatics

These programs are referenced in the context of the curriculum structure and requirements.

*Retrieved:* CS_MajorHandbook.pdf p.2 (0.71); CS_MajorHandbook.pdf p.11 (0.69); CS_MajorHandbook.pdf p.14 (0.68); CS_MajorHandbook.pdf p.6 (0.68); CS_MajorHandbook.pdf p.7 (0.68)  
*Retrieval hit:* False · *keyword score:* 0.0 · *latency:* 9.65s

### Q23 · qwen3.5:0.8b · off_topic
**Q:** Who won the 2022 FIFA World Cup?

**Reference:** Unrelated to the handbook; the chatbot should say it cannot find the information.

**Answer:** I could not find this in the documents.

*Retrieved:* (none)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 2.02s

### Q24 · qwen3.5:0.8b · off_topic
**Q:** Write a Python function that reverses a string.

**Reference:** Unrelated to the handbook; in strict mode the chatbot should decline.

**Answer:** I could not find this in the documents.

*Retrieved:* (none)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 0.29s

### Q25 · qwen3.5:0.8b · follow_up
*Asked after:* Tell me about CS311 Advanced Deep Learning.

**Q:** What is its prerequisite?

**Reference:** CS313 Deep Learning for AI ("its" = CS311 from the previous turn).

**Answer:** CS311 Advanced Deep Learning requires CS313 as a prerequisite.

*Retrieved:* CS_MajorHandbook.pdf p.18 (0.89); CS_MajorHandbook.pdf p.18 (0.82); CS_MajorHandbook.pdf p.18 (0.74); CS_MajorHandbook.pdf p.17 (0.72); CS_MajorHandbook.pdf p.13 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 8.71s

### Q26 · qwen3.5:0.8b · follow_up
*Asked after:* What are the prerequisites for CS 302 Algorithms & Theory of Computing?

**Q:** And how often is it offered?

**Reference:** Once a year ("it" = CS 302 from the previous turn).

**Answer:** CS302 is offered once a year.

[CS_MajorHandbook.pdf p.17]

*Retrieved:* CS_MajorHandbook.pdf p.17 (0.80); CS_MajorHandbook.pdf p.13 (0.74); CS_MajorHandbook.pdf p.17 (0.72); CS_MajorHandbook.pdf p.14 (0.72); CS_MajorHandbook.pdf p.12 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 8.77s

### Q27 · qwen3.5:0.8b · follow_up_off_topic
*Asked after:* What is the prerequisite for CS311 Advanced Deep Learning?

**Q:** Who won the 2022 FIFA World Cup?

**Reference:** Off-topic question asked right after a handbook question; the chatbot should still refuse.

**Answer:** I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.18 (0.71); CS_MajorHandbook.pdf p.18 (0.67); CS_MajorHandbook.pdf p.18 (0.63); CS_MajorHandbook.pdf p.15 (0.60); CS_MajorHandbook.pdf p.15 (0.60)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 8.62s

### Q01 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · program_requirements
**Q:** How many credits are required for the Computer Science major?

**Reference:** The major requires 56 credits.

**Answer:** The Computer Science major requires at least 56 credits to complete.

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.86); CS_MajorHandbook.pdf p.7 (0.80); CS_MajorHandbook.pdf p.2 (0.76); CS_MajorHandbook.pdf p.13 (0.76); CS_MajorHandbook.pdf p.4 (0.74)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 5.3s

### Q02 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · program_requirements
**Q:** Which courses are required for the Computer Science major?

**Reference:** CS 101, CS 201, CS 203, MATH 202, three intermediate courses, CS 302, four advanced courses, and Capstone I & II (or two additional intermediate/advanced courses).

**Answer:** To formally declare Computer Science as their major, the student must complete at least two Computer Science courses (MATH 202 - Discrete Math is also counted).

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.82); CS_MajorHandbook.pdf p.7 (0.78); CS_MajorHandbook.pdf p.8 (0.75); CS_MajorHandbook.pdf p.14 (0.75); CS_MajorHandbook.pdf p.4 (0.75)  
*Retrieval hit:* True · *keyword score:* 0.17 · *latency:* 5.21s

### Q03 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · academic_policies
**Q:** What must a student complete before formally declaring Computer Science as their major?

**Reference:** At least two Computer Science courses (MATH 202 Discrete Math also counts).

**Answer:** To formally declare Computer Science as their major, a student must complete at least two Computer Science courses (MATH 202 - Discrete Math is also counted).

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.81); CS_MajorHandbook.pdf p.1 (0.71); CS_MajorHandbook.pdf p.4 (0.70); CS_MajorHandbook.pdf p.14 (0.70); CS_MajorHandbook.pdf p.8 (0.70)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 5.25s

### Q04 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · program_requirements
**Q:** How many credits and courses does the Computer Science minor require?

**Reference:** 24 credits: six courses.

**Answer:** The Computer Science minor requires students to complete a total of six courses:

1. One programming course (4 credits)
2. One 100-level or 200-level CS course (4 credits)
3. Two intermediate courses (4 credits)
4. One 200-level or 300-level CS course (4 credits)
5. One advanced course (4 credits)

Total: 6 courses

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.88); CS_MajorHandbook.pdf p.7 (0.78); CS_MajorHandbook.pdf p.2 (0.76); CS_MajorHandbook.pdf p.13 (0.75); CS_MajorHandbook.pdf p.11 (0.75)  
*Retrieval hit:* True · *keyword score:* 0.5 · *latency:* 6.08s

### Q05 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · academic_policies
**Q:** What is required to declare a minor in Computer Science?

**Reference:** At least one Computer Science course (MATH 202 also counts).

**Answer:** To formally declare a minor in Computer Science, the student must complete at least one computer science course (MATH 202 - Discrete Math is also counted).

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.85); CS_MajorHandbook.pdf p.2 (0.69); CS_MajorHandbook.pdf p.1 (0.67); CS_MajorHandbook.pdf p.7 (0.65); CS_MajorHandbook.pdf p.11 (0.65)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 5.39s

### Q06 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · academic_policies
**Q:** What are the eligibility criteria for enrolling in CS 401 Capstone I?

**Reference:** A minimum major GPA of 3.5 and approval of a successful application.

**Answer:** A minimum major GPA of 3.5 and approval of a successful application are required for enrollment in CS 401 Capstone I.

*Retrieved:* CS_MajorHandbook.pdf p.9 (0.81); CS_MajorHandbook.pdf p.7 (0.63); CS_MajorHandbook.pdf p.8 (0.63); CS_MajorHandbook.pdf p.2 (0.62); CS_MajorHandbook.pdf p.13 (0.62)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 7.07s

### Q07 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · academic_policies
**Q:** What can students do instead of the capstone, and what is the consequence?

**Reference:** Take two additional intermediate or advanced courses; they graduate without honors (capstone = graduate with honors).

**Answer:** Students can also choose a concentration such as software engineering, artificial intelligence and machine learning, data science, business analytics. The Computer Science major at Fulbright is designed to prepare students for work in industry or continue their lifelong learning as well as potential graduate-level studies.

*Retrieved:* CS_MajorHandbook.pdf p.15 (0.61); CS_MajorHandbook.pdf p.12 (0.61); CS_MajorHandbook.pdf p.5 (0.59); CS_MajorHandbook.pdf p.4 (0.56); CS_MajorHandbook.pdf p.8 (0.56)  
*Retrieval hit:* True · *keyword score:* 0.0 · *latency:* 5.56s

### Q08 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · course_offerings
**Q:** What are the prerequisites for CS 302 Algorithms & Theory of Computing?

**Reference:** CS 201 and MATH 202.

**Answer:** CS 201

*Retrieved:* CS_MajorHandbook.pdf p.17 (0.80); CS_MajorHandbook.pdf p.17 (0.74); CS_MajorHandbook.pdf p.14 (0.72); CS_MajorHandbook.pdf p.12 (0.71); CS_MajorHandbook.pdf p.13 (0.70)  
*Retrieval hit:* True · *keyword score:* 0.5 · *latency:* 4.73s

### Q09 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · course_offerings
**Q:** What is the prerequisite for CS311 Advanced Deep Learning?

**Reference:** CS313 Deep Learning for AI.

**Answer:** CS313

*Retrieved:* CS_MajorHandbook.pdf p.18 (0.88); CS_MajorHandbook.pdf p.18 (0.80); CS_MajorHandbook.pdf p.18 (0.73); CS_MajorHandbook.pdf p.17 (0.71); CS_MajorHandbook.pdf p.13 (0.69)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 4.72s

### Q10 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · course_offerings
**Q:** How often is CS 210 Computer Networks offered?

**Reference:** Its availability is listed as 'On holding' (not currently scheduled).

**Answer:** On holding CS210

*Retrieved:* CS_MajorHandbook.pdf p.16 (0.75); CS_MajorHandbook.pdf p.13 (0.70); CS_MajorHandbook.pdf p.13 (0.66); CS_MajorHandbook.pdf p.17 (0.66); CS_MajorHandbook.pdf p.17 (0.63)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 4.67s

### Q11 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · course_offerings
**Q:** Which programming language is mainly used in CS 201 Data Structures & Algorithms?

**Reference:** Java (with some Python/C++ implementations).

**Answer:** Java

*Retrieved:* CS_MajorHandbook.pdf p.14 (0.79); CS_MajorHandbook.pdf p.14 (0.75); CS_MajorHandbook.pdf p.16 (0.74); CS_MajorHandbook.pdf p.17 (0.71); CS_MajorHandbook.pdf p.11 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 4.81s

### Q12 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · course_offerings
**Q:** What topics are covered in CS 211 Operating Systems?

**Reference:** Concurrency (processes, threads, scheduling, synchronization, deadlock), memory management (paging, segmentation, swapping), file systems, plus scalability, virtualization, security and distributed computing.

**Answer:** Concurrency, processes, threads, CPU scheduling, context switching, synchronization, and deadlock.

*Retrieved:* CS_MajorHandbook.pdf p.16 (0.79); CS_MajorHandbook.pdf p.16 (0.65); CS_MajorHandbook.pdf p.16 (0.65); CS_MajorHandbook.pdf p.14 (0.65); CS_MajorHandbook.pdf p.14 (0.64)  
*Retrieval hit:* True · *keyword score:* 0.33 · *latency:* 4.94s

### Q13 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · course_offerings
**Q:** Give some examples of advanced courses in the Computer Science major.

**Reference:** Foundations of Software Engineering, Database Systems, Computer Security, Cloud Computing, HCI, Computer Graphics, Game Design, Machine Learning, Deep Learning, Advanced Deep Learning, Computer Vision, NLP, Optimization, Computational Social Media, Bioinformatics.

**Answer:** • Advanced Algorithms & Theory of Computing
• Advanced Data Structures & Algorithms
• Advanced Discrete Mathematics
• Advanced Computer Organization

*Retrieved:* CS_MajorHandbook.pdf p.8 (0.81); CS_MajorHandbook.pdf p.11 (0.78); CS_MajorHandbook.pdf p.7 (0.77); CS_MajorHandbook.pdf p.8 (0.76); CS_MajorHandbook.pdf p.8 (0.74)  
*Retrieval hit:* True · *keyword score:* 0.0 · *latency:* 5.24s

### Q14 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · course_offerings
**Q:** In CS 207 Software Construction, what kind of applications do students build?

**Reference:** Android applications using Java.

**Answer:** Students build Android applications using Java.

*Retrieved:* CS_MajorHandbook.pdf p.15 (0.76); CS_MajorHandbook.pdf p.16 (0.72); CS_MajorHandbook.pdf p.15 (0.70); CS_MajorHandbook.pdf p.11 (0.69); CS_MajorHandbook.pdf p.14 (0.68)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 4.8s

### Q15 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · learning_outcomes
**Q:** What are the Major Learning Outcomes (MLOs) of the Computer Science program?

**Reference:** MLO1: understand fundamental CS (theory and systems); MLO2: explain emerging aspects of CS (AI, ML, data science...); MLO3: develop real-world applications.

**Answer:** The Major Learning Outcomes (MLOs) of the Computer Science program are:

1. Demonstrate an understanding of fundamental computer science by illustrating core concepts, comparing methods, analyzing and solving problems in both theory and systems.
2. Explain emerging aspects of the computer science discipline (e.g., artificial intelligence, machine learning, data science, business analytics, digital media, etc.).
3. Develop real-world applications (e.g., software systems and frameworks, mobile apps, data pipeline, etc.) by using knowledge of computer science and other disciplines.
4. Demonstrate an understanding of fundamental computer science by illustrating core concepts, comparing methods, analyzing and solving problems in both theory and systems.
5. Explain emerging aspects of the computer science discipline (e.g., artificial intelligence, machine learning, data science, business analytics, digital media, etc.).
6. Develop real-world applications (e.g., software systems and frameworks, mobile apps, data pipeline, etc.) by using knowledge of computer science and other disciplines.
7. Demonstrate an understanding of fundamental computer science by illustrating core concepts, comparing methods, analyzing and solving problems in both theory and systems.
8. Explain emerging aspects of the computer science discipline (e.g., artificial intelligence, machine learning, data science, business analytics, digital media, etc.).
9. Develop real-world applications (e.g., software systems and frameworks, mobile apps, data pipeline, etc.) by using knowledge of computer science and other disciplines.
10. Demonstrate an understanding of fundamental computer science by illustrating core concepts, comparing methods, analyzing and solving problems in both theory and systems.
11. Explain emerging aspects of the computer science discipline (e.g., artificial intelligence, machine learning, data science, business analytics, digital media, etc.).
12. Develop real-world applications (e.g., software systems and frameworks, mobile apps, data pipeline, etc.) by using knowledge of computer science and other disciplines.
13. Demonstrate an understanding of fundamental computer science by illustrating core concepts, comparing methods, analyzing and solving problems in both theory and systems.
14. Explain emerging aspects of the computer science discipline (e.g., artificial intelligence, machine learning, data science, business analytics, digital media, etc.).
15. Develop real-world applications (e.g., software systems and frameworks, mobile apps, data pipeline, etc.) by using knowledge of computer science and other disciplines.
16. Demonstrate an understanding of fundamental computer science by illustrating core concepts, comparing methods, analyzing and solving problems in both theory and systems.
17. Explain emerging aspects of the computer science discipline (e.g., artificial intelligence, machine learning, data science, business analytics, digital media, etc.).
18. Develop real-world applications (e.g., software systems and frameworks, mobile apps, data pipeline, etc.) by using knowledge of computer science and other disciplines.
19. Demonstrate an understanding of fundamental computer science by illustrating core concepts, comparing methods, analyzing and solving problems in both theory and systems.
20. Explain emerging aspects of the computer science discipline (e.g., artificial intelligence, machine learning, data science, business analytics, digital media, etc.).
21. Develop real-world applications (e.g., software systems and frameworks, mobile apps, data pipeline, etc.) by using knowledge of computer science and other disciplines.
22. Demonstrate an understanding of fundamental computer science by illustrating core concepts, comparing methods, analyzing and solving problems in both theory and systems.
23. Explain emerging aspects of the computer science discipline (e.g., artificial intelligence, machine learning, data science, business analytics, digital media, etc.).
24. Develop real-world applications (e.g., software systems and frameworks, mobile apps, data pipeline, etc.) by using knowledge of computer science and other disciplines.
25. Demonstrate an understanding of fundamental computer science by illustrating core concepts, comparing methods, analyzing and solving problems in both theory and systems.
26. Explain emerging aspects of the computer science discipline (e.g., artificial intelligence, machine learning, data science, business analytics, digital media, etc.).
27. Develop real-world applications (e.g., software systems and frameworks, mobile apps, data pipeline, etc.) by using knowledge of computer science and other disciplines.
28. Demonstrate an understanding of fundamental computer science by illustrating core concepts, comparing methods, analyzing and solving problems in both theory and systems.
29. Explain emerging aspects of the computer science discipline (e.g., artificial intelligence, machine learning, data science, business analytics, digital media, etc.).
30. Develop real-world applications (e.g., software systems and frameworks, mobile apps, data pipeline, etc.) by using knowledge of computer science and other disciplines.
31. Demonstrate an understanding of fundamental computer science by illustrating core concepts, comparing methods, analyzing and solving problems in both theory and systems.
32. Explain emerging aspects of the computer science discipline (e.g., artificial intelligence, machine learning, data science, business analytics,

*Retrieved:* CS_MajorHandbook.pdf p.5 (0.76); CS_MajorHandbook.pdf p.11 (0.73); CS_MajorHandbook.pdf p.4 (0.71); CS_MajorHandbook.pdf p.2 (0.70); CS_MajorHandbook.pdf p.4 (0.69)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 18.11s

### Q16 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · learning_outcomes
**Q:** What are the Program Educational Objectives (PEOs)?

**Reference:** PEO1: skills for employment or graduate school; PEO2: professional/personal ethics, collaboration and communication; PEO3: become innovators and thinkers solving CS challenges.

**Answer:** To equip students with the necessary skills and knowledge to gain employment in industry or study in graduate schools.

*Retrieved:* CS_MajorHandbook.pdf p.4 (0.80); CS_MajorHandbook.pdf p.4 (0.62); CS_MajorHandbook.pdf p.4 (0.59); CS_MajorHandbook.pdf p.11 (0.59); CS_MajorHandbook.pdf p.4 (0.57)  
*Retrieval hit:* True · *keyword score:* 0.33 · *latency:* 11.25s

### Q17 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · career
**Q:** What jobs have Computer Science graduates obtained?

**Reference:** Software engineer, testing engineer, AI engineer, data engineer, business analyst, product owner, product development manager.

**Answer:** Computer Science graduates have successfully obtained employment as software engineers, testing engineers, AI engineers, data engineers, business analysts, product owners, product development managers, and others.

*Retrieved:* CS_MajorHandbook.pdf p.6 (0.71); CS_MajorHandbook.pdf p.5 (0.70); CS_MajorHandbook.pdf p.2 (0.64); CS_MajorHandbook.pdf p.4 (0.63); CS_MajorHandbook.pdf p.14 (0.62)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 5.31s

### Q18 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · teaching_assessment
**Q:** How are students taught and assessed in the Computer Science major?

**Reference:** Active and collaborative learning; continuous formative assessment through discussion, in-class activities and applied learning, plus quizzes, exams, projects, presentations and the capstone.

**Answer:** Students are taught and assessed through a combination of lecture, lab, worksheet, group discussion, programming test, quiz, exam, group presentation, capstone, and other forms of formative assessment. They also have the opportunity to further focus their studies by selecting a concentration such as software engineering, artificial intelligence and machine learning, data science, business analytics.

*Retrieved:* CS_MajorHandbook.pdf p.12 (0.77); CS_MajorHandbook.pdf p.12 (0.74); CS_MajorHandbook.pdf p.4 (0.73); CS_MajorHandbook.pdf p.4 (0.72); CS_MajorHandbook.pdf p.14 (0.71)  
*Retrieval hit:* True · *keyword score:* 0.5 · *latency:* 6.11s

### Q19 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · program_requirements
**Q:** How many exploratory courses must students take, and how many can count toward the major?

**Reference:** 6 exploratory courses (24 credits); up to 2 courses (8 credits) can count toward the major.

**Answer:** 6 Exploratory courses (24 credits) can be counted toward the major.

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.76); CS_MajorHandbook.pdf p.7 (0.68); CS_MajorHandbook.pdf p.6 (0.67); CS_MajorHandbook.pdf p.13 (0.64); CS_MajorHandbook.pdf p.11 (0.63)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 4.76s

### Q20 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · ambiguous
**Q:** What degree is awarded after completing the degree requirements?

**Reference:** A B.S. in Computer Science. Note: the handbook's Degree Requirements section says 'Bachelor of Science in Applied Mathematics', an apparent copy-paste error that may mislead the model.

**Answer:** A Bachelor of Science in Applied Mathematics

*Retrieved:* CS_MajorHandbook.pdf p.6 (0.66); CS_MajorHandbook.pdf p.2 (0.62); CS_MajorHandbook.pdf p.3 (0.61); CS_MajorHandbook.pdf p.6 (0.60); CS_MajorHandbook.pdf p.5 (0.59)  
*Retrieval hit:* True · *keyword score:* 0.0 · *latency:* 12.1s

### Q21 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · out_of_scope
**Q:** What is the tuition fee for the Computer Science program?

**Reference:** Not stated in the handbook; the chatbot should say it cannot find the information.

**Answer:** The tuition fee for the Computer Science program is $10,000 per year.

*Retrieved:* CS_MajorHandbook.pdf p.2 (0.68); CS_MajorHandbook.pdf p.4 (0.65); CS_MajorHandbook.pdf p.19 (0.64); CS_MajorHandbook.pdf p.14 (0.64); CS_MajorHandbook.pdf p.4 (0.64)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 5.05s

### Q22 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · other
**Q:** Which universities' programs were used as references for the CS curriculum?

**Reference:** Stanford University, Carnegie Mellon University and Cornell University.

**Answer:** The University Mission, Vision, and Graduate Attributes 2 was referenced by the CS104: Introduction to Computer Science course, which aims at teaching students the basics of computer science, programming, and data science.

*Retrieved:* CS_MajorHandbook.pdf p.2 (0.71); CS_MajorHandbook.pdf p.11 (0.69); CS_MajorHandbook.pdf p.14 (0.68); CS_MajorHandbook.pdf p.6 (0.68); CS_MajorHandbook.pdf p.7 (0.68)  
*Retrieval hit:* False · *keyword score:* 0.0 · *latency:* 11.07s

### Q23 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · off_topic
**Q:** Who won the 2022 FIFA World Cup?

**Reference:** Unrelated to the handbook; the chatbot should say it cannot find the information.

**Answer:** I could not find this in the documents.

*Retrieved:* (none)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 1.61s

### Q24 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · off_topic
**Q:** Write a Python function that reverses a string.

**Reference:** Unrelated to the handbook; in strict mode the chatbot should decline.

**Answer:** I could not find this in the documents.

*Retrieved:* (none)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 0.25s

### Q25 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · follow_up
*Asked after:* Tell me about CS311 Advanced Deep Learning.

**Q:** What is its prerequisite?

**Reference:** CS313 Deep Learning for AI ("its" = CS311 from the previous turn).

**Answer:** CS313

*Retrieved:* CS_MajorHandbook.pdf p.18 (0.89); CS_MajorHandbook.pdf p.18 (0.82); CS_MajorHandbook.pdf p.18 (0.74); CS_MajorHandbook.pdf p.17 (0.72); CS_MajorHandbook.pdf p.13 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 4.91s

### Q26 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · follow_up
*Asked after:* What are the prerequisites for CS 302 Algorithms & Theory of Computing?

**Q:** And how often is it offered?

**Reference:** Once a year ("it" = CS 302 from the previous turn).

**Answer:** None (CS104 is recommended)

*Retrieved:* CS_MajorHandbook.pdf p.17 (0.80); CS_MajorHandbook.pdf p.13 (0.74); CS_MajorHandbook.pdf p.17 (0.72); CS_MajorHandbook.pdf p.14 (0.72); CS_MajorHandbook.pdf p.12 (0.71)  
*Retrieval hit:* True · *keyword score:* 0.0 · *latency:* 5.16s

### Q27 · hf.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF:Q8_0 · follow_up_off_topic
*Asked after:* What is the prerequisite for CS311 Advanced Deep Learning?

**Q:** Who won the 2022 FIFA World Cup?

**Reference:** Off-topic question asked right after a handbook question; the chatbot should still refuse.

**Answer:** The 2022 FIFA World Cup was won by South Korea and Japan.

*Retrieved:* CS_MajorHandbook.pdf p.18 (0.71); CS_MajorHandbook.pdf p.18 (0.67); CS_MajorHandbook.pdf p.18 (0.63); CS_MajorHandbook.pdf p.15 (0.60); CS_MajorHandbook.pdf p.15 (0.60)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 5.28s

### Q01 · llama3.2:3b · program_requirements
**Q:** How many credits are required for the Computer Science major?

**Reference:** The major requires 56 credits.

**Answer:** According to [CS_MajorHandbook.pdf p.6], Major Requirements (56 credits)

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.86); CS_MajorHandbook.pdf p.7 (0.80); CS_MajorHandbook.pdf p.2 (0.76); CS_MajorHandbook.pdf p.13 (0.76); CS_MajorHandbook.pdf p.4 (0.74)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 11.31s

### Q02 · llama3.2:3b · program_requirements
**Q:** Which courses are required for the Computer Science major?

**Reference:** CS 101, CS 201, CS 203, MATH 202, three intermediate courses, CS 302, four advanced courses, and Capstone I & II (or two additional intermediate/advanced courses).

**Answer:** According to [CS_MajorHandbook.pdf p.7], the required courses for the Computer Science major are:

• CS 101: Introduction to Programming (4 credits)
• CS 201: Data Structures & Algorithms (4 credits)
• MATH 202: Discrete Math (4 credits)
• Three intermediate courses (12 credits)
• Four advanced courses (16 credits)
• Capstone I and Capstone II (8 credits)

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.82); CS_MajorHandbook.pdf p.7 (0.78); CS_MajorHandbook.pdf p.8 (0.75); CS_MajorHandbook.pdf p.14 (0.75); CS_MajorHandbook.pdf p.4 (0.75)  
*Retrieval hit:* True · *keyword score:* 0.67 · *latency:* 9.24s

### Q03 · llama3.2:3b · academic_policies
**Q:** What must a student complete before formally declaring Computer Science as their major?

**Reference:** At least two Computer Science courses (MATH 202 Discrete Math also counts).

**Answer:** To formally declare Computer Science as their major, the student must complete at least two Computer Science courses (MATH 202 - Discrete Math is also counted). [CS_MajorHandbook.pdf p.7]

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.81); CS_MajorHandbook.pdf p.1 (0.71); CS_MajorHandbook.pdf p.4 (0.70); CS_MajorHandbook.pdf p.14 (0.70); CS_MajorHandbook.pdf p.8 (0.70)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 7.97s

### Q04 · llama3.2:3b · program_requirements
**Q:** How many credits and courses does the Computer Science minor require?

**Reference:** 24 credits: six courses.

**Answer:** The Computer Science minor requires 24 credits and a total of six courses:

• One programming course (4 credits)
• One 100-level or 200-level CS course (4 credits)
• CS 201 – Data Structures & Algorithms (4 credits)
• One intermediate course (4 credits)
• One 200-level or 300-level CS course (4 credits)
• One advanced course (4 credits)

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.88); CS_MajorHandbook.pdf p.7 (0.78); CS_MajorHandbook.pdf p.2 (0.76); CS_MajorHandbook.pdf p.13 (0.75); CS_MajorHandbook.pdf p.11 (0.75)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 13.09s

### Q05 · llama3.2:3b · academic_policies
**Q:** What is required to declare a minor in Computer Science?

**Reference:** At least one Computer Science course (MATH 202 also counts).

**Answer:** To formally declare a minor in Computer Science, the student must complete at least one Computer Science course (MATH 202 - Discrete Math is also counted). [CS_MajorHandbook.pdf p.6]

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.85); CS_MajorHandbook.pdf p.2 (0.69); CS_MajorHandbook.pdf p.1 (0.67); CS_MajorHandbook.pdf p.7 (0.65); CS_MajorHandbook.pdf p.11 (0.65)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 8.08s

### Q06 · llama3.2:3b · academic_policies
**Q:** What are the eligibility criteria for enrolling in CS 401 Capstone I?

**Reference:** A minimum major GPA of 3.5 and approval of a successful application.

**Answer:** Eligibility criteria for enrollment in CS 401 include a minimum major GPA of 3.5 and approval of a successful application. [CS_MajorHandbook.pdf p.9]

*Retrieved:* CS_MajorHandbook.pdf p.9 (0.81); CS_MajorHandbook.pdf p.7 (0.63); CS_MajorHandbook.pdf p.8 (0.63); CS_MajorHandbook.pdf p.2 (0.62); CS_MajorHandbook.pdf p.13 (0.62)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 8.31s

### Q07 · llama3.2:3b · academic_policies
**Q:** What can students do instead of the capstone, and what is the consequence?

**Reference:** Take two additional intermediate or advanced courses; they graduate without honors (capstone = graduate with honors).

**Answer:** I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.15 (0.61); CS_MajorHandbook.pdf p.12 (0.61); CS_MajorHandbook.pdf p.5 (0.59); CS_MajorHandbook.pdf p.4 (0.56); CS_MajorHandbook.pdf p.8 (0.56)  
*Retrieval hit:* True · *keyword score:* 0.0 · *latency:* 7.42s

### Q08 · llama3.2:3b · course_offerings
**Q:** What are the prerequisites for CS 302 Algorithms & Theory of Computing?

**Reference:** CS 201 and MATH 202.

**Answer:** The prerequisites for CS 302 Algorithms & Theory of Computing are CS201 and MATH 202.

*Retrieved:* CS_MajorHandbook.pdf p.17 (0.80); CS_MajorHandbook.pdf p.17 (0.74); CS_MajorHandbook.pdf p.14 (0.72); CS_MajorHandbook.pdf p.12 (0.71); CS_MajorHandbook.pdf p.13 (0.70)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 7.81s

### Q09 · llama3.2:3b · course_offerings
**Q:** What is the prerequisite for CS311 Advanced Deep Learning?

**Reference:** CS313 Deep Learning for AI.

**Answer:** The prerequisite for CS311: Advanced Deep Learning is CS313 [CS_MajorHandbook.pdf p.18].

*Retrieved:* CS_MajorHandbook.pdf p.18 (0.88); CS_MajorHandbook.pdf p.18 (0.80); CS_MajorHandbook.pdf p.18 (0.73); CS_MajorHandbook.pdf p.17 (0.71); CS_MajorHandbook.pdf p.13 (0.69)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 12.24s

### Q10 · llama3.2:3b · course_offerings
**Q:** How often is CS 210 Computer Networks offered?

**Reference:** Its availability is listed as 'On holding' (not currently scheduled).

**Answer:** CS210: Computer Networks is offered on holding CS201.

*Retrieved:* CS_MajorHandbook.pdf p.16 (0.75); CS_MajorHandbook.pdf p.13 (0.70); CS_MajorHandbook.pdf p.13 (0.66); CS_MajorHandbook.pdf p.17 (0.66); CS_MajorHandbook.pdf p.17 (0.63)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 7.25s

### Q11 · llama3.2:3b · course_offerings
**Q:** Which programming language is mainly used in CS 201 Data Structures & Algorithms?

**Reference:** Java (with some Python/C++ implementations).

**Answer:** Java is the main programming language used in the course, but some Python/C++ implementations are also introduced.

*Retrieved:* CS_MajorHandbook.pdf p.14 (0.79); CS_MajorHandbook.pdf p.14 (0.75); CS_MajorHandbook.pdf p.16 (0.74); CS_MajorHandbook.pdf p.17 (0.71); CS_MajorHandbook.pdf p.11 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 7.44s

### Q12 · llama3.2:3b · course_offerings
**Q:** What topics are covered in CS 211 Operating Systems?

**Reference:** Concurrency (processes, threads, scheduling, synchronization, deadlock), memory management (paging, segmentation, swapping), file systems, plus scalability, virtualization, security and distributed computing.

**Answer:** The course CS211: Operating Systems covers three main parts:

* Concurrency, covering topics such as:
	+ Processes
	+ Threads
	+ CPU scheduling
	+ Context switching
	+ Synchronization
	+ Deadlock
* Memory management issues, including:
	+ Linking
	+ Allocation
	+ Address translation
	+ Segmentation
	+ Paging
	+ Swapping
* File systems, discussing:
	+ Disk management
	+ File organization
	+ Crash recovery

*Retrieved:* CS_MajorHandbook.pdf p.16 (0.79); CS_MajorHandbook.pdf p.16 (0.65); CS_MajorHandbook.pdf p.16 (0.65); CS_MajorHandbook.pdf p.14 (0.65); CS_MajorHandbook.pdf p.14 (0.64)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 9.35s

### Q13 · llama3.2:3b · course_offerings
**Q:** Give some examples of advanced courses in the Computer Science major.

**Reference:** Foundations of Software Engineering, Database Systems, Computer Security, Cloud Computing, HCI, Computer Graphics, Game Design, Machine Learning, Deep Learning, Advanced Deep Learning, Computer Vision, NLP, Optimization, Computational Social Media, Bioinformatics.

**Answer:** Here are some examples of Advanced Courses in the Computer Science major:

• Foundations of Software Engineering
• Database Systems
• Computer Security
• Cloud Computing
• Human-Computer Interaction
• Computer Graphics
• Game Design & Development
• Machine Learning
• Deep Learning
• Advanced Deep Learning
• Computer Vision
• Natural Language Processing
• Optimization
• Computational Social Media

*Retrieved:* CS_MajorHandbook.pdf p.8 (0.81); CS_MajorHandbook.pdf p.11 (0.78); CS_MajorHandbook.pdf p.7 (0.77); CS_MajorHandbook.pdf p.8 (0.76); CS_MajorHandbook.pdf p.8 (0.74)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 8.69s

### Q14 · llama3.2:3b · course_offerings
**Q:** In CS 207 Software Construction, what kind of applications do students build?

**Reference:** Android applications using Java.

**Answer:** Students in CS 207 Software Construction will build Android applications using Java. [CS_MajorHandbook.pdf p.15]

*Retrieved:* CS_MajorHandbook.pdf p.15 (0.76); CS_MajorHandbook.pdf p.16 (0.72); CS_MajorHandbook.pdf p.15 (0.70); CS_MajorHandbook.pdf p.11 (0.69); CS_MajorHandbook.pdf p.14 (0.68)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 8.71s

### Q15 · llama3.2:3b · learning_outcomes
**Q:** What are the Major Learning Outcomes (MLOs) of the Computer Science program?

**Reference:** MLO1: understand fundamental CS (theory and systems); MLO2: explain emerging aspects of CS (AI, ML, data science...); MLO3: develop real-world applications.

**Answer:** The Major Learning Outcomes (MLOs) of the Computer Science program are:

* MLO 1: Demonstrate an understanding of fundamental computer science by illustrating core concepts, comparing methods, analyzing and solving problems in both theory and systems.
* MLO 2: Explain emerging aspects of the computer science discipline (e.g., artificial intelligence, machine learning, data science, business analytics, digital media, etc.).
* MLO 3: Develop real-world applications (e.g., software systems and frameworks, mobile apps, data pipeline, etc.) by using knowledge of computer science and other disciplines.

*Retrieved:* CS_MajorHandbook.pdf p.5 (0.76); CS_MajorHandbook.pdf p.11 (0.73); CS_MajorHandbook.pdf p.4 (0.71); CS_MajorHandbook.pdf p.2 (0.70); CS_MajorHandbook.pdf p.4 (0.69)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 10.05s

### Q16 · llama3.2:3b · learning_outcomes
**Q:** What are the Program Educational Objectives (PEOs)?

**Reference:** PEO1: skills for employment or graduate school; PEO2: professional/personal ethics, collaboration and communication; PEO3: become innovators and thinkers solving CS challenges.

**Answer:** The Program Educational Objectives (PEOs) are:

1. To equip students with the necessary skills and knowledge to gain employment in industry or
2. To ingrain in students a strong code of professional and personal ethics, and the ability to
effectively and creatively collaborate and communicate in the workplace and beyond.
3. To cultivate students to become innovators and thinkers to solve computer science related challenges.

*Retrieved:* CS_MajorHandbook.pdf p.4 (0.80); CS_MajorHandbook.pdf p.4 (0.62); CS_MajorHandbook.pdf p.4 (0.59); CS_MajorHandbook.pdf p.11 (0.59); CS_MajorHandbook.pdf p.4 (0.57)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 15.19s

### Q17 · llama3.2:3b · career
**Q:** What jobs have Computer Science graduates obtained?

**Reference:** Software engineer, testing engineer, AI engineer, data engineer, business analyst, product owner, product development manager.

**Answer:** According to [CS_MajorHandbook.pdf p.3], graduates with the B.S. Computer Science have successfully gained employment as:

• Software engineer
• Testing engineer
• AI engineer
• Data engineer
• Business analyst
• Product owner
• Product development manager

*Retrieved:* CS_MajorHandbook.pdf p.6 (0.71); CS_MajorHandbook.pdf p.5 (0.70); CS_MajorHandbook.pdf p.2 (0.64); CS_MajorHandbook.pdf p.4 (0.63); CS_MajorHandbook.pdf p.14 (0.62)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 8.4s

### Q18 · llama3.2:3b · teaching_assessment
**Q:** How are students taught and assessed in the Computer Science major?

**Reference:** Active and collaborative learning; continuous formative assessment through discussion, in-class activities and applied learning, plus quizzes, exams, projects, presentations and the capstone.

**Answer:** Teaching and assessment in the Computer Science major are designed on the principle of active and collaborative learning. In addition to summative methods, courses rely on continuous formative assessment of student learning through discussion (instructor-led and student-led), in-class activities, and applied learning.

---

The program learning outcomes for teaching and learning methods include:

1. Lecture
2. Lab
3. Worksheet
4. Group discussion
5. Programming test
6. Quiz
7. Exam
8. Group presentation

These methods are used to assess examples of student learning in the following areas:

1. Demonstrate an understanding of fundamental computer science by illustrating core concepts, comparing methods, analyzing and solving problems in both theory and systems.
2. Explain emerging aspects of the computer science discipline (e.g., artificial intelligence, machine learning, data science, business analytics, digital media, etc.).
3. Develop real-world applications (e.g., software systems and frameworks, mobile apps, data pipeline, etc.) by using lecture, lab, field trip, class project, presentation, and capstone.

*Retrieved:* CS_MajorHandbook.pdf p.12 (0.77); CS_MajorHandbook.pdf p.12 (0.74); CS_MajorHandbook.pdf p.4 (0.73); CS_MajorHandbook.pdf p.4 (0.72); CS_MajorHandbook.pdf p.14 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 12.4s

### Q19 · llama3.2:3b · program_requirements
**Q:** How many exploratory courses must students take, and how many can count toward the major?

**Reference:** 6 exploratory courses (24 credits); up to 2 courses (8 credits) can count toward the major.

**Answer:** Students must take 6 exploratory courses (24 credits). Among these 6 courses, up to 2 courses (8 credits) can be counted toward the major. [CS_MajorHandbook.pdf p.7]

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.76); CS_MajorHandbook.pdf p.7 (0.68); CS_MajorHandbook.pdf p.6 (0.67); CS_MajorHandbook.pdf p.13 (0.64); CS_MajorHandbook.pdf p.11 (0.63)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 14.19s

### Q20 · llama3.2:3b · ambiguous
**Q:** What degree is awarded after completing the degree requirements?

**Reference:** A B.S. in Computer Science. Note: the handbook's Degree Requirements section says 'Bachelor of Science in Applied Mathematics', an apparent copy-paste error that may mislead the model.

**Answer:** A Bachelor of Science in Applied Mathematics is awarded following the successful completion of the General Curriculum Requirements and Major Requirements.

*Retrieved:* CS_MajorHandbook.pdf p.6 (0.66); CS_MajorHandbook.pdf p.2 (0.62); CS_MajorHandbook.pdf p.3 (0.61); CS_MajorHandbook.pdf p.6 (0.60); CS_MajorHandbook.pdf p.5 (0.59)  
*Retrieval hit:* True · *keyword score:* 0.0 · *latency:* 7.21s

### Q21 · llama3.2:3b · out_of_scope
**Q:** What is the tuition fee for the Computer Science program?

**Reference:** Not stated in the handbook; the chatbot should say it cannot find the information.

**Answer:** I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.2 (0.68); CS_MajorHandbook.pdf p.4 (0.65); CS_MajorHandbook.pdf p.19 (0.64); CS_MajorHandbook.pdf p.14 (0.64); CS_MajorHandbook.pdf p.4 (0.64)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 14.96s

### Q22 · llama3.2:3b · other
**Q:** Which universities' programs were used as references for the CS curriculum?

**Reference:** Stanford University, Carnegie Mellon University and Cornell University.

**Answer:** I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.2 (0.71); CS_MajorHandbook.pdf p.11 (0.69); CS_MajorHandbook.pdf p.14 (0.68); CS_MajorHandbook.pdf p.6 (0.68); CS_MajorHandbook.pdf p.7 (0.68)  
*Retrieval hit:* False · *keyword score:* 0.0 · *latency:* 6.91s

### Q23 · llama3.2:3b · off_topic
**Q:** Who won the 2022 FIFA World Cup?

**Reference:** Unrelated to the handbook; the chatbot should say it cannot find the information.

**Answer:** I could not find this in the documents.

*Retrieved:* (none)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 7.98s

### Q24 · llama3.2:3b · off_topic
**Q:** Write a Python function that reverses a string.

**Reference:** Unrelated to the handbook; in strict mode the chatbot should decline.

**Answer:** I could not find this in the documents.

*Retrieved:* (none)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 0.35s

### Q25 · llama3.2:3b · follow_up
*Asked after:* Tell me about CS311 Advanced Deep Learning.

**Q:** What is its prerequisite?

**Reference:** CS313 Deep Learning for AI ("its" = CS311 from the previous turn).

**Answer:** CS311: Advanced Deep Learning has CS313 as a prerequisite.

*Retrieved:* CS_MajorHandbook.pdf p.18 (0.89); CS_MajorHandbook.pdf p.18 (0.82); CS_MajorHandbook.pdf p.18 (0.74); CS_MajorHandbook.pdf p.17 (0.72); CS_MajorHandbook.pdf p.13 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 7.6s

### Q26 · llama3.2:3b · follow_up
*Asked after:* What are the prerequisites for CS 302 Algorithms & Theory of Computing?

**Q:** And how often is it offered?

**Reference:** Once a year ("it" = CS 302 from the previous turn).

**Answer:** It is offered once a year.

*Retrieved:* CS_MajorHandbook.pdf p.17 (0.80); CS_MajorHandbook.pdf p.13 (0.74); CS_MajorHandbook.pdf p.17 (0.72); CS_MajorHandbook.pdf p.14 (0.72); CS_MajorHandbook.pdf p.12 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 7.27s

### Q27 · llama3.2:3b · follow_up_off_topic
*Asked after:* What is the prerequisite for CS311 Advanced Deep Learning?

**Q:** Who won the 2022 FIFA World Cup?

**Reference:** Off-topic question asked right after a handbook question; the chatbot should still refuse.

**Answer:** I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.18 (0.71); CS_MajorHandbook.pdf p.18 (0.67); CS_MajorHandbook.pdf p.18 (0.63); CS_MajorHandbook.pdf p.15 (0.60); CS_MajorHandbook.pdf p.15 (0.60)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 7.51s

### Q01 · qwen2.5:3b · program_requirements
**Q:** How many credits are required for the Computer Science major?

**Reference:** The major requires 56 credits.

**Answer:** The major requires 56 credits.

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.86); CS_MajorHandbook.pdf p.7 (0.80); CS_MajorHandbook.pdf p.2 (0.76); CS_MajorHandbook.pdf p.13 (0.76); CS_MajorHandbook.pdf p.4 (0.74)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 6.78s

### Q02 · qwen2.5:3b · program_requirements
**Q:** Which courses are required for the Computer Science major?

**Reference:** CS 101, CS 201, CS 203, MATH 202, three intermediate courses, CS 302, four advanced courses, and Capstone I & II (or two additional intermediate/advanced courses).

**Answer:** The required courses for the Computer Science major include:

- CS 101: Introduction to Programming (or CS 103 or CS 104)
- MATH 202: Discrete Math
- CS 201: Data Structures & Algorithms
- CS 203: Computer Organization
- Three intermediate courses
- CS 302: Algorithms & Theory of Computing
- Four advanced courses

Additionally, students must complete six minor requirements and fulfill the experiential learning and compulsory course requirements.

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.82); CS_MajorHandbook.pdf p.7 (0.78); CS_MajorHandbook.pdf p.8 (0.75); CS_MajorHandbook.pdf p.14 (0.75); CS_MajorHandbook.pdf p.4 (0.75)  
*Retrieval hit:* True · *keyword score:* 0.83 · *latency:* 14.17s

### Q03 · qwen2.5:3b · academic_policies
**Q:** What must a student complete before formally declaring Computer Science as their major?

**Reference:** At least two Computer Science courses (MATH 202 Discrete Math also counts).

**Answer:** I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.81); CS_MajorHandbook.pdf p.1 (0.71); CS_MajorHandbook.pdf p.4 (0.70); CS_MajorHandbook.pdf p.14 (0.70); CS_MajorHandbook.pdf p.8 (0.70)  
*Retrieval hit:* True · *keyword score:* 0.0 · *latency:* 6.71s

### Q04 · qwen2.5:3b · program_requirements
**Q:** How many credits and courses does the Computer Science minor require?

**Reference:** 24 credits: six courses.

**Answer:** The Computer Science minor requires 24 credits and consists of six courses.

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.88); CS_MajorHandbook.pdf p.7 (0.78); CS_MajorHandbook.pdf p.2 (0.76); CS_MajorHandbook.pdf p.13 (0.75); CS_MajorHandbook.pdf p.11 (0.75)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 6.23s

### Q05 · qwen2.5:3b · academic_policies
**Q:** What is required to declare a minor in Computer Science?

**Reference:** At least one Computer Science course (MATH 202 also counts).

**Answer:** To formally declare a minor in Computer Science, the student must complete at least one Computer Science course (MATH 202 - Discrete Math is also counted).

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.85); CS_MajorHandbook.pdf p.2 (0.69); CS_MajorHandbook.pdf p.1 (0.67); CS_MajorHandbook.pdf p.7 (0.65); CS_MajorHandbook.pdf p.11 (0.65)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 6.91s

### Q06 · qwen2.5:3b · academic_policies
**Q:** What are the eligibility criteria for enrolling in CS 401 Capstone I?

**Reference:** A minimum major GPA of 3.5 and approval of a successful application.

**Answer:** Eligibility criteria for enrollment in CS 401: Capstone I include a minimum major GPA of 3.5 and approval of a successful application.

*Retrieved:* CS_MajorHandbook.pdf p.9 (0.81); CS_MajorHandbook.pdf p.7 (0.63); CS_MajorHandbook.pdf p.8 (0.63); CS_MajorHandbook.pdf p.2 (0.62); CS_MajorHandbook.pdf p.13 (0.62)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 7.06s

### Q07 · qwen2.5:3b · academic_policies
**Q:** What can students do instead of the capstone, and what is the consequence?

**Reference:** Take two additional intermediate or advanced courses; they graduate without honors (capstone = graduate with honors).

**Answer:** I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.15 (0.61); CS_MajorHandbook.pdf p.12 (0.61); CS_MajorHandbook.pdf p.5 (0.59); CS_MajorHandbook.pdf p.4 (0.56); CS_MajorHandbook.pdf p.8 (0.56)  
*Retrieval hit:* True · *keyword score:* 0.0 · *latency:* 6.25s

### Q08 · qwen2.5:3b · course_offerings
**Q:** What are the prerequisites for CS 302 Algorithms & Theory of Computing?

**Reference:** CS 201 and MATH 202.

**Answer:** The prerequisites for CS 302 Algorithms & Theory of Computing are CS201 and MATH 202.

*Retrieved:* CS_MajorHandbook.pdf p.17 (0.80); CS_MajorHandbook.pdf p.17 (0.74); CS_MajorHandbook.pdf p.14 (0.72); CS_MajorHandbook.pdf p.12 (0.71); CS_MajorHandbook.pdf p.13 (0.70)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 6.63s

### Q09 · qwen2.5:3b · course_offerings
**Q:** What is the prerequisite for CS311 Advanced Deep Learning?

**Reference:** CS313 Deep Learning for AI.

**Answer:** CS311: Advanced Deep Learning has a prerequisite of CS313.

*Retrieved:* CS_MajorHandbook.pdf p.18 (0.88); CS_MajorHandbook.pdf p.18 (0.80); CS_MajorHandbook.pdf p.18 (0.73); CS_MajorHandbook.pdf p.17 (0.71); CS_MajorHandbook.pdf p.13 (0.69)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 6.25s

### Q10 · qwen2.5:3b · course_offerings
**Q:** How often is CS 210 Computer Networks offered?

**Reference:** Its availability is listed as 'On holding' (not currently scheduled).

**Answer:** On holding

*Retrieved:* CS_MajorHandbook.pdf p.16 (0.75); CS_MajorHandbook.pdf p.13 (0.70); CS_MajorHandbook.pdf p.13 (0.66); CS_MajorHandbook.pdf p.17 (0.66); CS_MajorHandbook.pdf p.17 (0.63)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 6.1s

### Q11 · qwen2.5:3b · course_offerings
**Q:** Which programming language is mainly used in CS 201 Data Structures & Algorithms?

**Reference:** Java (with some Python/C++ implementations).

**Answer:** Java is the main programming language used in the course.

*Retrieved:* CS_MajorHandbook.pdf p.14 (0.79); CS_MajorHandbook.pdf p.14 (0.75); CS_MajorHandbook.pdf p.16 (0.74); CS_MajorHandbook.pdf p.17 (0.71); CS_MajorHandbook.pdf p.11 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 6.2s

### Q12 · qwen2.5:3b · course_offerings
**Q:** What topics are covered in CS 211 Operating Systems?

**Reference:** Concurrency (processes, threads, scheduling, synchronization, deadlock), memory management (paging, segmentation, swapping), file systems, plus scalability, virtualization, security and distributed computing.

**Answer:** CS211 covers fundamental concepts and principles of modern operating systems, including concurrency (processes, threads, CPU scheduling, context switching, synchronization, and deadlock), memory management issues (linking, allocation, address translation, segmentation, paging, and swapping), and file systems (disk management, file organization, and crash recovery). After these three main parts, the course will introduce advanced topics such as scalability, virtualization, security, and support for distributed computing.

*Retrieved:* CS_MajorHandbook.pdf p.16 (0.79); CS_MajorHandbook.pdf p.16 (0.65); CS_MajorHandbook.pdf p.16 (0.65); CS_MajorHandbook.pdf p.14 (0.65); CS_MajorHandbook.pdf p.14 (0.64)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 8.07s

### Q13 · qwen2.5:3b · course_offerings
**Q:** Give some examples of advanced courses in the Computer Science major.

**Reference:** Foundations of Software Engineering, Database Systems, Computer Security, Cloud Computing, HCI, Computer Graphics, Game Design, Machine Learning, Deep Learning, Advanced Deep Learning, Computer Vision, NLP, Optimization, Computational Social Media, Bioinformatics.

**Answer:** Sample Advanced Courses include:
- Foundations of Software Engineering
- Database Systems
- Computer Security
- Cloud Computing
- Human-Computer Interaction
- Computer Graphics
- Game Design & Development
- Machine Learning
- Deep Learning
- Advanced Deep Learning
- Computer Vision
- Natural Language Processing
- Optimization
- Computational Social Media

*Retrieved:* CS_MajorHandbook.pdf p.8 (0.81); CS_MajorHandbook.pdf p.11 (0.78); CS_MajorHandbook.pdf p.7 (0.77); CS_MajorHandbook.pdf p.8 (0.76); CS_MajorHandbook.pdf p.8 (0.74)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 8.03s

### Q14 · qwen2.5:3b · course_offerings
**Q:** In CS 207 Software Construction, what kind of applications do students build?

**Reference:** Android applications using Java.

**Answer:** Students build Android applications using Java.

*Retrieved:* CS_MajorHandbook.pdf p.15 (0.76); CS_MajorHandbook.pdf p.16 (0.72); CS_MajorHandbook.pdf p.15 (0.70); CS_MajorHandbook.pdf p.11 (0.69); CS_MajorHandbook.pdf p.14 (0.68)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 6.59s

### Q15 · qwen2.5:3b · learning_outcomes
**Q:** What are the Major Learning Outcomes (MLOs) of the Computer Science program?

**Reference:** MLO1: understand fundamental CS (theory and systems); MLO2: explain emerging aspects of CS (AI, ML, data science...); MLO3: develop real-world applications.

**Answer:** The Major Learning Outcomes (MLOs) for the Computer Science program are:

- MLO 1: Demonstrate an understanding of fundamental computer science by illustrating core concepts, comparing methods, analyzing and solving problems in both theory and systems.
- MLO 2: Explain emerging aspects of the computer science discipline (e.g., artificial intelligence, machine learning, data science, business analytics, digital media, etc.).
- MLO 3: Develop real-world applications (e.g., software systems and frameworks, mobile apps, data pipeline, etc.) by using knowledge of computer science and other disciplines.

*Retrieved:* CS_MajorHandbook.pdf p.5 (0.76); CS_MajorHandbook.pdf p.11 (0.73); CS_MajorHandbook.pdf p.4 (0.71); CS_MajorHandbook.pdf p.2 (0.70); CS_MajorHandbook.pdf p.4 (0.69)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 9.04s

### Q16 · qwen2.5:3b · learning_outcomes
**Q:** What are the Program Educational Objectives (PEOs)?

**Reference:** PEO1: skills for employment or graduate school; PEO2: professional/personal ethics, collaboration and communication; PEO3: become innovators and thinkers solving CS challenges.

**Answer:** Program Educational Objectives (PEOs) include:
- PEO1: To equip students with the necessary skills and knowledge to gain employment in industry or to study in graduate schools.
- PEO2: To ingrain in students a strong code of professional and personal ethics, and the ability to effectively and creatively collaborate and communicate in the workplace and beyond.
- PEO3: To cultivate students to become innovators and thinkers to solve computer science related challenges.

*Retrieved:* CS_MajorHandbook.pdf p.4 (0.80); CS_MajorHandbook.pdf p.4 (0.62); CS_MajorHandbook.pdf p.4 (0.59); CS_MajorHandbook.pdf p.11 (0.59); CS_MajorHandbook.pdf p.4 (0.57)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 8.51s

### Q17 · qwen2.5:3b · career
**Q:** What jobs have Computer Science graduates obtained?

**Reference:** Software engineer, testing engineer, AI engineer, data engineer, business analyst, product owner, product development manager.

**Answer:** Graduates with the B.S. Computer Science have successfully gained employment as:

- Software engineer
- Testing engineer
- AI engineer
- Data engineer
- Business analyst
- Product owner
- Product development manager

[I could not find this in the documents.]

*Retrieved:* CS_MajorHandbook.pdf p.6 (0.71); CS_MajorHandbook.pdf p.5 (0.70); CS_MajorHandbook.pdf p.2 (0.64); CS_MajorHandbook.pdf p.4 (0.63); CS_MajorHandbook.pdf p.14 (0.62)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 7.54s

### Q18 · qwen2.5:3b · teaching_assessment
**Q:** How are students taught and assessed in the Computer Science major?

**Reference:** Active and collaborative learning; continuous formative assessment through discussion, in-class activities and applied learning, plus quizzes, exams, projects, presentations and the capstone.

**Answer:** Students at Fulbright are taught through a combination of lecture, lab, field trip, class project, presentation, and direct experiences in projects and problems. Assessment methods include quizzes, exams, group discussions, group presentations, and capstone projects. Continuous formative assessment is also provided through discussion (instructor-led and student-led), in-class activities, and applied learning.

*Retrieved:* CS_MajorHandbook.pdf p.12 (0.77); CS_MajorHandbook.pdf p.12 (0.74); CS_MajorHandbook.pdf p.4 (0.73); CS_MajorHandbook.pdf p.4 (0.72); CS_MajorHandbook.pdf p.14 (0.71)  
*Retrieval hit:* True · *keyword score:* 0.5 · *latency:* 8.17s

### Q19 · qwen2.5:3b · program_requirements
**Q:** How many exploratory courses must students take, and how many can count toward the major?

**Reference:** 6 exploratory courses (24 credits); up to 2 courses (8 credits) can count toward the major.

**Answer:** Students must take 6 exploratory courses (24 credits), with up to 2 of these courses counting toward the major (8 credits).

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.76); CS_MajorHandbook.pdf p.7 (0.68); CS_MajorHandbook.pdf p.6 (0.67); CS_MajorHandbook.pdf p.13 (0.64); CS_MajorHandbook.pdf p.11 (0.63)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 7.35s

### Q20 · qwen2.5:3b · ambiguous
**Q:** What degree is awarded after completing the degree requirements?

**Reference:** A B.S. in Computer Science. Note: the handbook's Degree Requirements section says 'Bachelor of Science in Applied Mathematics', an apparent copy-paste error that may mislead the model.

**Answer:** A Bachelor of Science in Applied Mathematics is awarded.

*Retrieved:* CS_MajorHandbook.pdf p.6 (0.66); CS_MajorHandbook.pdf p.2 (0.62); CS_MajorHandbook.pdf p.3 (0.61); CS_MajorHandbook.pdf p.6 (0.60); CS_MajorHandbook.pdf p.5 (0.59)  
*Retrieval hit:* True · *keyword score:* 0.0 · *latency:* 6.13s

### Q21 · qwen2.5:3b · out_of_scope
**Q:** What is the tuition fee for the Computer Science program?

**Reference:** Not stated in the handbook; the chatbot should say it cannot find the information.

**Answer:** I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.2 (0.68); CS_MajorHandbook.pdf p.4 (0.65); CS_MajorHandbook.pdf p.19 (0.64); CS_MajorHandbook.pdf p.14 (0.64); CS_MajorHandbook.pdf p.4 (0.64)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 6.07s

### Q22 · qwen2.5:3b · other
**Q:** Which universities' programs were used as references for the CS curriculum?

**Reference:** Stanford University, Carnegie Mellon University and Cornell University.

**Answer:** I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.2 (0.71); CS_MajorHandbook.pdf p.11 (0.69); CS_MajorHandbook.pdf p.14 (0.68); CS_MajorHandbook.pdf p.6 (0.68); CS_MajorHandbook.pdf p.7 (0.68)  
*Retrieval hit:* False · *keyword score:* 0.0 · *latency:* 6.13s

### Q23 · qwen2.5:3b · off_topic
**Q:** Who won the 2022 FIFA World Cup?

**Reference:** Unrelated to the handbook; the chatbot should say it cannot find the information.

**Answer:** I could not find this in the documents.

*Retrieved:* (none)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 1.76s

### Q24 · qwen2.5:3b · off_topic
**Q:** Write a Python function that reverses a string.

**Reference:** Unrelated to the handbook; in strict mode the chatbot should decline.

**Answer:** I could not find this in the documents.

*Retrieved:* (none)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 0.25s

### Q25 · qwen2.5:3b · follow_up
*Asked after:* Tell me about CS311 Advanced Deep Learning.

**Q:** What is its prerequisite?

**Reference:** CS313 Deep Learning for AI ("its" = CS311 from the previous turn).

**Answer:** CS311 Advanced Deep Learning has a prerequisite of CS313.

*Retrieved:* CS_MajorHandbook.pdf p.18 (0.89); CS_MajorHandbook.pdf p.18 (0.82); CS_MajorHandbook.pdf p.18 (0.74); CS_MajorHandbook.pdf p.17 (0.72); CS_MajorHandbook.pdf p.13 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 7.15s

### Q26 · qwen2.5:3b · follow_up
*Asked after:* What are the prerequisites for CS 302 Algorithms & Theory of Computing?

**Q:** And how often is it offered?

**Reference:** Once a year ("it" = CS 302 from the previous turn).

**Answer:** I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.17 (0.80); CS_MajorHandbook.pdf p.13 (0.74); CS_MajorHandbook.pdf p.17 (0.72); CS_MajorHandbook.pdf p.14 (0.72); CS_MajorHandbook.pdf p.12 (0.71)  
*Retrieval hit:* True · *keyword score:* 0.0 · *latency:* 6.57s

### Q27 · qwen2.5:3b · follow_up_off_topic
*Asked after:* What is the prerequisite for CS311 Advanced Deep Learning?

**Q:** Who won the 2022 FIFA World Cup?

**Reference:** Off-topic question asked right after a handbook question; the chatbot should still refuse.

**Answer:** I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.18 (0.71); CS_MajorHandbook.pdf p.18 (0.67); CS_MajorHandbook.pdf p.18 (0.63); CS_MajorHandbook.pdf p.15 (0.60); CS_MajorHandbook.pdf p.15 (0.60)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 6.64s

### Q01 · gemma3:4b · program_requirements
**Q:** How many credits are required for the Computer Science major?

**Reference:** The major requires 56 credits.

**Answer:** The Computer Science major requires 56 credits [CS_MajorHandbook.pdf p.6].

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.86); CS_MajorHandbook.pdf p.7 (0.80); CS_MajorHandbook.pdf p.2 (0.76); CS_MajorHandbook.pdf p.13 (0.76); CS_MajorHandbook.pdf p.4 (0.74)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 9.84s

### Q02 · gemma3:4b · program_requirements
**Q:** Which courses are required for the Computer Science major?

**Reference:** CS 101, CS 201, CS 203, MATH 202, three intermediate courses, CS 302, four advanced courses, and Capstone I & II (or two additional intermediate/advanced courses).

**Answer:** Here are the required courses for the Computer Science major, according to the documents:

*   CS 101: Introduction to Programming (4 credits)
*   CS 201: Data Structures & Algorithms (4 credits)
*   CS 203: Computer Organization (4 credits)
*   MATH 202: Discrete Math (4 credits)
*   Three intermediate courses (12 credits)
*   CS 302: Algorithms & Theory of Computing (4 credits)
*   Four advanced courses (16 credits)
*   Capstone I and Capstone II (8 credits) [or alternative options] [CS_MajorHandbook.pdf p.7]

[CS_MajorHandbook.pdf p.7]

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.82); CS_MajorHandbook.pdf p.7 (0.78); CS_MajorHandbook.pdf p.8 (0.75); CS_MajorHandbook.pdf p.14 (0.75); CS_MajorHandbook.pdf p.4 (0.75)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 13.83s

### Q03 · gemma3:4b · academic_policies
**Q:** What must a student complete before formally declaring Computer Science as their major?

**Reference:** At least two Computer Science courses (MATH 202 Discrete Math also counts).

**Answer:** To formally declare Computer Science as their major, the student must complete at least two Computer Science courses (MATH 202 - Discrete Math is also counted) [CS_MajorHandbook.pdf p.7].

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.81); CS_MajorHandbook.pdf p.1 (0.71); CS_MajorHandbook.pdf p.4 (0.70); CS_MajorHandbook.pdf p.14 (0.70); CS_MajorHandbook.pdf p.8 (0.70)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 10.01s

### Q04 · gemma3:4b · program_requirements
**Q:** How many credits and courses does the Computer Science minor require?

**Reference:** 24 credits: six courses.

**Answer:** The Computer Science minor requires 24 credits and consists of six courses:

*   One programming course (CS 101, CS 103, or CS 104)
*   One 100-level or 200-level CS course
*   CS 201 – Data Structures & Algorithms
*   One intermediate course
*   One 200-level or 300-level CS course
*   One advanced course [CS_MajorHandbook.pdf p.7]

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.88); CS_MajorHandbook.pdf p.7 (0.78); CS_MajorHandbook.pdf p.2 (0.76); CS_MajorHandbook.pdf p.13 (0.75); CS_MajorHandbook.pdf p.11 (0.75)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 12.56s

### Q05 · gemma3:4b · academic_policies
**Q:** What is required to declare a minor in Computer Science?

**Reference:** At least one Computer Science course (MATH 202 also counts).

**Answer:** To formally declare a minor in Computer Science, the student must complete at least one Computer Science course (MATH 202 - Discrete Math is also counted). [CS_MajorHandbook.pdf p.7]

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.85); CS_MajorHandbook.pdf p.2 (0.69); CS_MajorHandbook.pdf p.1 (0.67); CS_MajorHandbook.pdf p.7 (0.65); CS_MajorHandbook.pdf p.11 (0.65)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 10.45s

### Q06 · gemma3:4b · academic_policies
**Q:** What are the eligibility criteria for enrolling in CS 401 Capstone I?

**Reference:** A minimum major GPA of 3.5 and approval of a successful application.

**Answer:** Eligibility criteria for enrollment in CS 401: Capstone I include a minimum major GPA of 3.5 and approval of a successful application [CS_MajorHandbook.pdf p.9].

*Retrieved:* CS_MajorHandbook.pdf p.9 (0.81); CS_MajorHandbook.pdf p.7 (0.63); CS_MajorHandbook.pdf p.8 (0.63); CS_MajorHandbook.pdf p.2 (0.62); CS_MajorHandbook.pdf p.13 (0.62)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 10.26s

### Q07 · gemma3:4b · academic_policies
**Q:** What can students do instead of the capstone, and what is the consequence?

**Reference:** Take two additional intermediate or advanced courses; they graduate without honors (capstone = graduate with honors).

**Answer:** [CS_MajorHandbook.pdf p.12] Students can complete a group presentation instead of a capstone. However, the documents do not specify the consequence of not completing a capstone [CS_MajorHandbook.pdf p.12].

*Retrieved:* CS_MajorHandbook.pdf p.15 (0.61); CS_MajorHandbook.pdf p.12 (0.61); CS_MajorHandbook.pdf p.5 (0.59); CS_MajorHandbook.pdf p.4 (0.56); CS_MajorHandbook.pdf p.8 (0.56)  
*Retrieval hit:* True · *keyword score:* 0.5 · *latency:* 10.48s

### Q08 · gemma3:4b · course_offerings
**Q:** What are the prerequisites for CS 302 Algorithms & Theory of Computing?

**Reference:** CS 201 and MATH 202.

**Answer:** CS302: Algorithms & Theory of Computing
Prerequisites: CS201 & MATH 202 [CS_MajorHandbook.pdf p.17]

*Retrieved:* CS_MajorHandbook.pdf p.17 (0.80); CS_MajorHandbook.pdf p.17 (0.74); CS_MajorHandbook.pdf p.14 (0.72); CS_MajorHandbook.pdf p.12 (0.71); CS_MajorHandbook.pdf p.13 (0.70)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 10.36s

### Q09 · gemma3:4b · course_offerings
**Q:** What is the prerequisite for CS311 Advanced Deep Learning?

**Reference:** CS313 Deep Learning for AI.

**Answer:** The prerequisite for CS311 Advanced Deep Learning is CS313 [CS_MajorHandbook.pdf p.18].

*Retrieved:* CS_MajorHandbook.pdf p.18 (0.88); CS_MajorHandbook.pdf p.18 (0.80); CS_MajorHandbook.pdf p.18 (0.73); CS_MajorHandbook.pdf p.17 (0.71); CS_MajorHandbook.pdf p.13 (0.69)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 10.33s

### Q10 · gemma3:4b · course_offerings
**Q:** How often is CS 210 Computer Networks offered?

**Reference:** Its availability is listed as 'On holding' (not currently scheduled).

**Answer:** CS210 is “On holding” [CS_MajorHandbook.pdf p.13]. [CS_MajorHandbook.pdf p.16] states that CS210 has a prerequisite of CS201. I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.16 (0.75); CS_MajorHandbook.pdf p.13 (0.70); CS_MajorHandbook.pdf p.13 (0.66); CS_MajorHandbook.pdf p.17 (0.66); CS_MajorHandbook.pdf p.17 (0.63)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 11.01s

### Q11 · gemma3:4b · course_offerings
**Q:** Which programming language is mainly used in CS 201 Data Structures & Algorithms?

**Reference:** Java (with some Python/C++ implementations).

**Answer:** Java is the main programming language used in the course [CS_MajorHandbook.pdf p.14].

*Retrieved:* CS_MajorHandbook.pdf p.14 (0.79); CS_MajorHandbook.pdf p.14 (0.75); CS_MajorHandbook.pdf p.16 (0.74); CS_MajorHandbook.pdf p.17 (0.71); CS_MajorHandbook.pdf p.11 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 10.06s

### Q12 · gemma3:4b · course_offerings
**Q:** What topics are covered in CS 211 Operating Systems?

**Reference:** Concurrency (processes, threads, scheduling, synchronization, deadlock), memory management (paging, segmentation, swapping), file systems, plus scalability, virtualization, security and distributed computing.

**Answer:** CS211: Operating Systems
Prerequisites: CS201

The course is divided into three main parts:

*   Concurrency (processes, threads, CPU scheduling, context switching, synchronization, and deadlock)
*   Memory Management (linking, allocation, address translation, segmentation, paging, and swapping)
*   File Systems (disk management, file organization, and crash recovery) [CS_MajorHandbook.pdf p.16]

*Retrieved:* CS_MajorHandbook.pdf p.16 (0.79); CS_MajorHandbook.pdf p.16 (0.65); CS_MajorHandbook.pdf p.16 (0.65); CS_MajorHandbook.pdf p.14 (0.65); CS_MajorHandbook.pdf p.14 (0.64)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 11.88s

### Q13 · gemma3:4b · course_offerings
**Q:** Give some examples of advanced courses in the Computer Science major.

**Reference:** Foundations of Software Engineering, Database Systems, Computer Security, Cloud Computing, HCI, Computer Graphics, Game Design, Machine Learning, Deep Learning, Advanced Deep Learning, Computer Vision, NLP, Optimization, Computational Social Media, Bioinformatics.

**Answer:** Here are some examples of advanced courses in the Computer Science major:

*   Foundations of Software Engineering [CS_MajorHandbook.pdf p.8]
*   Database Systems [CS_MajorHandbook.pdf p.8]
*   Computer Security [CS_MajorHandbook.pdf p.8]
*   Cloud Computing [CS_MajorHandbook.pdf p.8]
*   Human-Computer Interaction [CS_MajorHandbook.pdf p.8]
*   Computer Graphics [CS_MajorHandbook.pdf p.8]
*   Game Design & Development [CS_MajorHandbook.pdf p.8]
*   Machine Learning [CS_MajorHandbook.pdf p.8]
*   Deep Learning [CS_MajorHandbook.pdf p.8]
*   Advanced Deep Learning [CS_MajorHandbook.pdf p.8]
*   Computer Vision [CS_MajorHandbook.pdf p.8]
*   Natural Language Processing [CS_MajorHandbook.pdf p.8]
*   Optimization [CS_MajorHandbook.pdf p.8]
*   Computational Social Media [CS_MajorHandbook.pdf p.8] [CS_MajorHandbook.pdf p.8]

*Retrieved:* CS_MajorHandbook.pdf p.8 (0.81); CS_MajorHandbook.pdf p.11 (0.78); CS_MajorHandbook.pdf p.7 (0.77); CS_MajorHandbook.pdf p.8 (0.76); CS_MajorHandbook.pdf p.8 (0.74)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 16.82s

### Q14 · gemma3:4b · course_offerings
**Q:** In CS 207 Software Construction, what kind of applications do students build?

**Reference:** Android applications using Java.

**Answer:** Students will work in teams to practice designing software using UML models such as use-case, sequence, and class diagrams. They will also implement the design via building Android applications using Java [CS_MajorHandbook.pdf p.15].

*Retrieved:* CS_MajorHandbook.pdf p.15 (0.76); CS_MajorHandbook.pdf p.16 (0.72); CS_MajorHandbook.pdf p.15 (0.70); CS_MajorHandbook.pdf p.11 (0.69); CS_MajorHandbook.pdf p.14 (0.68)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 10.97s

### Q15 · gemma3:4b · learning_outcomes
**Q:** What are the Major Learning Outcomes (MLOs) of the Computer Science program?

**Reference:** MLO1: understand fundamental CS (theory and systems); MLO2: explain emerging aspects of CS (AI, ML, data science...); MLO3: develop real-world applications.

**Answer:** Here are the Major Learning Outcomes (MLOs) of the Computer Science program:

*   MLO 1 Demonstrate an understanding of fundamental computer science by illustrating core concepts, comparing methods, analyzing and solving problems in both theory and systems.
*   MLO 2 Explain emerging aspects of the computer science discipline (e.g., artificial intelligence, machine learning, data science, business analytics, digital media, etc.).
*   MLO 3 Develop real-world applications (e.g., software systems and frameworks, mobile apps, data pipeline, etc.) by using knowledge of computer science and other disciplines. [CS_MajorHandbook.pdf p.5]

*Retrieved:* CS_MajorHandbook.pdf p.5 (0.76); CS_MajorHandbook.pdf p.11 (0.73); CS_MajorHandbook.pdf p.4 (0.71); CS_MajorHandbook.pdf p.2 (0.70); CS_MajorHandbook.pdf p.4 (0.69)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 13.53s

### Q16 · gemma3:4b · learning_outcomes
**Q:** What are the Program Educational Objectives (PEOs)?

**Reference:** PEO1: skills for employment or graduate school; PEO2: professional/personal ethics, collaboration and communication; PEO3: become innovators and thinkers solving CS challenges.

**Answer:** PEO1. To equip students with the necessary skills and knowledge to gain employment in industry or to study in graduate schools. [CS_MajorHandbook.pdf p.4]
PEO2. To ingrain in students a strong code of professional and personal ethics, and the ability to effectively and creatively collaborate and communicate in the workplace and beyond. [CS_MajorHandbook.pdf p.4]
PEO3. To cultivate students to become innovators and thinkers to solve computer science related challenges. [CS_MajorHandbook.pdf p.4]

*Retrieved:* CS_MajorHandbook.pdf p.4 (0.80); CS_MajorHandbook.pdf p.4 (0.62); CS_MajorHandbook.pdf p.4 (0.59); CS_MajorHandbook.pdf p.11 (0.59); CS_MajorHandbook.pdf p.4 (0.57)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 12.95s

### Q17 · gemma3:4b · career
**Q:** What jobs have Computer Science graduates obtained?

**Reference:** Software engineer, testing engineer, AI engineer, data engineer, business analyst, product owner, product development manager.

**Answer:** Graduates with the B.S. Computer Science have successfully gained employment as:

• Software engineer
• Testing engineer
• AI engineer
• Data engineer
• Business analyst
• Product owner
• Product development manager [CS_MajorHandbook.pdf p.3]

*Retrieved:* CS_MajorHandbook.pdf p.6 (0.71); CS_MajorHandbook.pdf p.5 (0.70); CS_MajorHandbook.pdf p.2 (0.64); CS_MajorHandbook.pdf p.4 (0.63); CS_MajorHandbook.pdf p.14 (0.62)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 11.33s

### Q18 · gemma3:4b · teaching_assessment
**Q:** How are students taught and assessed in the Computer Science major?

**Reference:** Active and collaborative learning; continuous formative assessment through discussion, in-class activities and applied learning, plus quizzes, exams, projects, presentations and the capstone.

**Answer:** Teaching and assessment in the Computer Science major are designed on the principle of active and collaborative learning. In addition to summative methods, courses rely on continuous formative assessment of student learning through discussion (instructor-led and student-led), in-class activities, and applied learning. [CS_MajorHandbook.pdf p.12]

*Retrieved:* CS_MajorHandbook.pdf p.12 (0.77); CS_MajorHandbook.pdf p.12 (0.74); CS_MajorHandbook.pdf p.4 (0.73); CS_MajorHandbook.pdf p.4 (0.72); CS_MajorHandbook.pdf p.14 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 11.64s

### Q19 · gemma3:4b · program_requirements
**Q:** How many exploratory courses must students take, and how many can count toward the major?

**Reference:** 6 exploratory courses (24 credits); up to 2 courses (8 credits) can count toward the major.

**Answer:** Students must take 6 exploratory courses (24 credits). Up to 2 of these courses (8 credits) can be counted toward the major [CS_MajorHandbook.pdf p.7].

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.76); CS_MajorHandbook.pdf p.7 (0.68); CS_MajorHandbook.pdf p.6 (0.67); CS_MajorHandbook.pdf p.13 (0.64); CS_MajorHandbook.pdf p.11 (0.63)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 11.2s

### Q20 · gemma3:4b · ambiguous
**Q:** What degree is awarded after completing the degree requirements?

**Reference:** A B.S. in Computer Science. Note: the handbook's Degree Requirements section says 'Bachelor of Science in Applied Mathematics', an apparent copy-paste error that may mislead the model.

**Answer:** A Bachelor of Science in Applied Mathematics is awarded following the successful completion of: [CS_MajorHandbook.pdf p.6]

*Retrieved:* CS_MajorHandbook.pdf p.6 (0.66); CS_MajorHandbook.pdf p.2 (0.62); CS_MajorHandbook.pdf p.3 (0.61); CS_MajorHandbook.pdf p.6 (0.60); CS_MajorHandbook.pdf p.5 (0.59)  
*Retrieval hit:* True · *keyword score:* 0.0 · *latency:* 10.35s

### Q21 · gemma3:4b · out_of_scope
**Q:** What is the tuition fee for the Computer Science program?

**Reference:** Not stated in the handbook; the chatbot should say it cannot find the information.

**Answer:** I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.2 (0.68); CS_MajorHandbook.pdf p.4 (0.65); CS_MajorHandbook.pdf p.19 (0.64); CS_MajorHandbook.pdf p.14 (0.64); CS_MajorHandbook.pdf p.4 (0.64)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 9.67s

### Q22 · gemma3:4b · other
**Q:** Which universities' programs were used as references for the CS curriculum?

**Reference:** Stanford University, Carnegie Mellon University and Cornell University.

**Answer:** These programs include:

• MSc/PhD Computer Science
• MSc Data Science
• MSc Bioinformatics [CS_MajorHandbook.pdf p.6]

*Retrieved:* CS_MajorHandbook.pdf p.2 (0.71); CS_MajorHandbook.pdf p.11 (0.69); CS_MajorHandbook.pdf p.14 (0.68); CS_MajorHandbook.pdf p.6 (0.68); CS_MajorHandbook.pdf p.7 (0.68)  
*Retrieval hit:* False · *keyword score:* 0.0 · *latency:* 10.4s

### Q23 · gemma3:4b · off_topic
**Q:** Who won the 2022 FIFA World Cup?

**Reference:** Unrelated to the handbook; the chatbot should say it cannot find the information.

**Answer:** I could not find this in the documents.

*Retrieved:* (none)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 2.0s

### Q24 · gemma3:4b · off_topic
**Q:** Write a Python function that reverses a string.

**Reference:** Unrelated to the handbook; in strict mode the chatbot should decline.

**Answer:** I could not find this in the documents.

*Retrieved:* (none)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 0.25s

### Q25 · gemma3:4b · follow_up
*Asked after:* Tell me about CS311 Advanced Deep Learning.

**Q:** What is its prerequisite?

**Reference:** CS313 Deep Learning for AI ("its" = CS311 from the previous turn).

**Answer:** CS313 [CS_MajorHandbook.pdf p.18]

*Retrieved:* CS_MajorHandbook.pdf p.18 (0.89); CS_MajorHandbook.pdf p.18 (0.82); CS_MajorHandbook.pdf p.18 (0.74); CS_MajorHandbook.pdf p.17 (0.72); CS_MajorHandbook.pdf p.13 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 9.9s

### Q26 · gemma3:4b · follow_up
*Asked after:* What are the prerequisites for CS 302 Algorithms & Theory of Computing?

**Q:** And how often is it offered?

**Reference:** Once a year ("it" = CS 302 from the previous turn).

**Answer:** Once a year [CS_MajorHandbook.pdf p.17]

*Retrieved:* CS_MajorHandbook.pdf p.17 (0.80); CS_MajorHandbook.pdf p.13 (0.74); CS_MajorHandbook.pdf p.17 (0.72); CS_MajorHandbook.pdf p.14 (0.72); CS_MajorHandbook.pdf p.12 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 10.32s

### Q27 · gemma3:4b · follow_up_off_topic
*Asked after:* What is the prerequisite for CS311 Advanced Deep Learning?

**Q:** Who won the 2022 FIFA World Cup?

**Reference:** Off-topic question asked right after a handbook question; the chatbot should still refuse.

**Answer:** I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.18 (0.71); CS_MajorHandbook.pdf p.18 (0.67); CS_MajorHandbook.pdf p.18 (0.63); CS_MajorHandbook.pdf p.15 (0.60); CS_MajorHandbook.pdf p.15 (0.60)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 9.88s

### Q01 · qwen3.5:9b · program_requirements
**Q:** How many credits are required for the Computer Science major?

**Reference:** The major requires 56 credits.

**Answer:** The Computer Science major requires a total of 56 credits for major requirements. This includes specific compulsory courses, intermediate courses, advanced courses, and capstone projects as outlined in the document.

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.86); CS_MajorHandbook.pdf p.7 (0.80); CS_MajorHandbook.pdf p.2 (0.76); CS_MajorHandbook.pdf p.13 (0.76); CS_MajorHandbook.pdf p.4 (0.74)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 17.02s

### Q02 · qwen3.5:9b · program_requirements
**Q:** Which courses are required for the Computer Science major?

**Reference:** CS 101, CS 201, CS 203, MATH 202, three intermediate courses, CS 302, four advanced courses, and Capstone I & II (or two additional intermediate/advanced courses).

**Answer:** The required courses for the Computer Science major include:
- CS 101: Introduction to Programming (4 credits)
- CS 201: Data Structures & Algorithms (4 credits)
- CS 203: Computer Organization (4 credits)
- MATH 202: Discrete Math (4 credits)
- Three intermediate courses (12 credits)
- CS 302: Algorithms & Theory of Computing (4 credits)
- Four advanced courses (16 credits)
- Capstone I and Capstone II (8 credits) [CS_MajorHandbook.pdf p.7]

Alternatively, students may choose:
- Two additional intermediate courses (8 credits)
- Two additional advanced courses (8 credits)
- One additional intermediate course and one additional advanced course (8 credits) [CS_MajorHandbook.pdf p.7]

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.82); CS_MajorHandbook.pdf p.7 (0.78); CS_MajorHandbook.pdf p.8 (0.75); CS_MajorHandbook.pdf p.14 (0.75); CS_MajorHandbook.pdf p.4 (0.75)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 24.34s

### Q03 · qwen3.5:9b · academic_policies
**Q:** What must a student complete before formally declaring Computer Science as their major?

**Reference:** At least two Computer Science courses (MATH 202 Discrete Math also counts).

**Answer:** To formally declare Computer Science as their major, a student must complete at least two Computer Science courses. Note that MATH 202 (Discrete Math) also counts toward this requirement [CS_MajorHandbook.pdf p.7].

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.81); CS_MajorHandbook.pdf p.1 (0.71); CS_MajorHandbook.pdf p.4 (0.70); CS_MajorHandbook.pdf p.14 (0.70); CS_MajorHandbook.pdf p.8 (0.70)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 16.06s

### Q04 · qwen3.5:9b · program_requirements
**Q:** How many credits and courses does the Computer Science minor require?

**Reference:** 24 credits: six courses.

**Answer:** The Computer Science minor requires a total of 24 credits, consisting of six courses:
- One programming course (4 credits)
- One 100-level or 200-level CS course (4 credits)
- CS 201 – Data Structures & Algorithms (4 credits)
- One intermediate course (4 credits)
- One 200-level or 300-level CS course (4 credits)
- One advanced course (4 credits) [CS_MajorHandbook.pdf p.7].

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.88); CS_MajorHandbook.pdf p.7 (0.78); CS_MajorHandbook.pdf p.2 (0.76); CS_MajorHandbook.pdf p.13 (0.75); CS_MajorHandbook.pdf p.11 (0.75)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 20.18s

### Q05 · qwen3.5:9b · academic_policies
**Q:** What is required to declare a minor in Computer Science?

**Reference:** At least one Computer Science course (MATH 202 also counts).

**Answer:** To formally declare a minor in Computer Science, the student must complete at least one Computer Science course (MATH 202 - Discrete Math is also counted) [CS_MajorHandbook.pdf p.7]. The minor requires a total of six courses totaling 24 credits, including:
- One programming course (4 credits)
- One 100-level or 200-level CS course (4 credits)
- CS 201 – Data Structures & Algorithms (4 credits)
- One intermediate course (4 credits)
- One 200-level or 300-level CS course (4 credits)
- One advanced course (4 credits) [CS_MajorHandbook.pdf p.7].

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.85); CS_MajorHandbook.pdf p.2 (0.69); CS_MajorHandbook.pdf p.1 (0.67); CS_MajorHandbook.pdf p.7 (0.65); CS_MajorHandbook.pdf p.11 (0.65)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 22.59s

### Q06 · qwen3.5:9b · academic_policies
**Q:** What are the eligibility criteria for enrolling in CS 401 Capstone I?

**Reference:** A minimum major GPA of 3.5 and approval of a successful application.

**Answer:** To enroll in CS 401: Capstone I, students must meet the following eligibility criteria:
- A minimum major GPA of 3.5.
- Approval of a successful application.

These details are found in [CS_MajorHandbook.pdf p.9].

*Retrieved:* CS_MajorHandbook.pdf p.9 (0.81); CS_MajorHandbook.pdf p.7 (0.63); CS_MajorHandbook.pdf p.8 (0.63); CS_MajorHandbook.pdf p.2 (0.62); CS_MajorHandbook.pdf p.13 (0.62)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 17.29s

### Q07 · qwen3.5:9b · academic_policies
**Q:** What can students do instead of the capstone, and what is the consequence?

**Reference:** Take two additional intermediate or advanced courses; they graduate without honors (capstone = graduate with honors).

**Answer:** I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.15 (0.61); CS_MajorHandbook.pdf p.12 (0.61); CS_MajorHandbook.pdf p.5 (0.59); CS_MajorHandbook.pdf p.4 (0.56); CS_MajorHandbook.pdf p.8 (0.56)  
*Retrieval hit:* True · *keyword score:* 0.0 · *latency:* 13.73s

### Q08 · qwen3.5:9b · course_offerings
**Q:** What are the prerequisites for CS 302 Algorithms & Theory of Computing?

**Reference:** CS 201 and MATH 202.

**Answer:** The prerequisites for CS302 Algorithms & Theory of Computing are CS201 and MATH202 [CS_MajorHandbook.pdf p.17].

*Retrieved:* CS_MajorHandbook.pdf p.17 (0.80); CS_MajorHandbook.pdf p.17 (0.74); CS_MajorHandbook.pdf p.14 (0.72); CS_MajorHandbook.pdf p.12 (0.71); CS_MajorHandbook.pdf p.13 (0.70)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 16.11s

### Q09 · qwen3.5:9b · course_offerings
**Q:** What is the prerequisite for CS311 Advanced Deep Learning?

**Reference:** CS313 Deep Learning for AI.

**Answer:** The prerequisite for CS311 Advanced Deep Learning is CS313 [CS_MajorHandbook.pdf p.18].

*Retrieved:* CS_MajorHandbook.pdf p.18 (0.88); CS_MajorHandbook.pdf p.18 (0.80); CS_MajorHandbook.pdf p.18 (0.73); CS_MajorHandbook.pdf p.17 (0.71); CS_MajorHandbook.pdf p.13 (0.69)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 14.86s

### Q10 · qwen3.5:9b · course_offerings
**Q:** How often is CS 210 Computer Networks offered?

**Reference:** Its availability is listed as 'On holding' (not currently scheduled).

**Answer:** Based on the provided context, CS 210 Computer Networks is listed as "On holding" in the availability column [CS_MajorHandbook.pdf p.13]. The document does not specify a standard frequency like "once a year" or "twice a year" for this specific course.

*Retrieved:* CS_MajorHandbook.pdf p.16 (0.75); CS_MajorHandbook.pdf p.13 (0.70); CS_MajorHandbook.pdf p.13 (0.66); CS_MajorHandbook.pdf p.17 (0.66); CS_MajorHandbook.pdf p.17 (0.63)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 18.04s

### Q11 · qwen3.5:9b · course_offerings
**Q:** Which programming language is mainly used in CS 201 Data Structures & Algorithms?

**Reference:** Java (with some Python/C++ implementations).

**Answer:** Java is the main programming language used in CS201, though some Python/C++ implementations are also introduced [CS_MajorHandbook.pdf p.14].

*Retrieved:* CS_MajorHandbook.pdf p.14 (0.79); CS_MajorHandbook.pdf p.14 (0.75); CS_MajorHandbook.pdf p.16 (0.74); CS_MajorHandbook.pdf p.17 (0.71); CS_MajorHandbook.pdf p.11 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 15.51s

### Q12 · qwen3.5:9b · course_offerings
**Q:** What topics are covered in CS 211 Operating Systems?

**Reference:** Concurrency (processes, threads, scheduling, synchronization, deadlock), memory management (paging, segmentation, swapping), file systems, plus scalability, virtualization, security and distributed computing.

**Answer:** CS211: Operating Systems covers three main parts:
- Concurrency: processes, threads, CPU scheduling, context switching, synchronization, and deadlock.
- Memory management: linking, allocation, address translation, segmentation, paging, and swapping.
- File systems: disk management, file organization, and crash recovery.
The course also concludes with advanced topics such as scalability, virtualization, security, and support for distributed computing. [CS_MajorHandbook.pdf p.16]

*Retrieved:* CS_MajorHandbook.pdf p.16 (0.79); CS_MajorHandbook.pdf p.16 (0.65); CS_MajorHandbook.pdf p.16 (0.65); CS_MajorHandbook.pdf p.14 (0.65); CS_MajorHandbook.pdf p.14 (0.64)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 18.88s

### Q13 · qwen3.5:9b · course_offerings
**Q:** Give some examples of advanced courses in the Computer Science major.

**Reference:** Foundations of Software Engineering, Database Systems, Computer Security, Cloud Computing, HCI, Computer Graphics, Game Design, Machine Learning, Deep Learning, Advanced Deep Learning, Computer Vision, NLP, Optimization, Computational Social Media, Bioinformatics.

**Answer:** Here are some examples of advanced courses in the Computer Science major:

- Foundations of Software Engineering
- Database Systems
- Computer Security
- Cloud Computing
- Human-Computer Interaction
- Computer Graphics
- Game Design & Development
- Machine Learning
- Deep Learning
- Advanced Deep Learning
- Computer Vision
- Natural Language Processing
- Optimization
- Computational Social Media

[CS_MajorHandbook.pdf p.8]

*Retrieved:* CS_MajorHandbook.pdf p.8 (0.81); CS_MajorHandbook.pdf p.11 (0.78); CS_MajorHandbook.pdf p.7 (0.77); CS_MajorHandbook.pdf p.8 (0.76); CS_MajorHandbook.pdf p.8 (0.74)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 18.89s

### Q14 · qwen3.5:9b · course_offerings
**Q:** In CS 207 Software Construction, what kind of applications do students build?

**Reference:** Android applications using Java.

**Answer:** In CS207 Software Construction, students build **Android applications using Java** to implement their software designs [CS_MajorHandbook.pdf p.15].

*Retrieved:* CS_MajorHandbook.pdf p.15 (0.76); CS_MajorHandbook.pdf p.16 (0.72); CS_MajorHandbook.pdf p.15 (0.70); CS_MajorHandbook.pdf p.11 (0.69); CS_MajorHandbook.pdf p.14 (0.68)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 15.44s

### Q15 · qwen3.5:9b · learning_outcomes
**Q:** What are the Major Learning Outcomes (MLOs) of the Computer Science program?

**Reference:** MLO1: understand fundamental CS (theory and systems); MLO2: explain emerging aspects of CS (AI, ML, data science...); MLO3: develop real-world applications.

**Answer:** The Major Learning Outcomes (MLOs) for the Computer Science program are:

*   **MLO 1:** Demonstrate an understanding of fundamental computer science by illustrating core concepts, comparing methods, analyzing and solving problems in both theory and systems.
*   **MLO 2:** Explain emerging aspects of the computer science discipline (e.g., artificial intelligence, machine learning, data science, business analytics, digital media, etc.).
*   **MLO 3:** Develop real-world applications (e.g., software systems and frameworks, mobile apps, data pipeline, etc.) by using knowledge of computer science and other disciplines.

[CS_MajorHandbook.pdf p.5]

*Retrieved:* CS_MajorHandbook.pdf p.5 (0.76); CS_MajorHandbook.pdf p.11 (0.73); CS_MajorHandbook.pdf p.4 (0.71); CS_MajorHandbook.pdf p.2 (0.70); CS_MajorHandbook.pdf p.4 (0.69)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 22.18s

### Q16 · qwen3.5:9b · learning_outcomes
**Q:** What are the Program Educational Objectives (PEOs)?

**Reference:** PEO1: skills for employment or graduate school; PEO2: professional/personal ethics, collaboration and communication; PEO3: become innovators and thinkers solving CS challenges.

**Answer:** The Program Educational Objectives (PEOs) are:
- PEO1: To equip students with the necessary skills and knowledge to gain employment in industry or to study in graduate schools.
- PEO2: To ingrain in students a strong code of professional and personal ethics, and the ability to effectively and creatively collaborate and communicate in the workplace and beyond.
- PEO3: To cultivate students to become innovators and thinkers to solve computer science related challenges.

[CS_MajorHandbook.pdf p.4]

*Retrieved:* CS_MajorHandbook.pdf p.4 (0.80); CS_MajorHandbook.pdf p.4 (0.62); CS_MajorHandbook.pdf p.4 (0.59); CS_MajorHandbook.pdf p.11 (0.59); CS_MajorHandbook.pdf p.4 (0.57)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 20.22s

### Q17 · qwen3.5:9b · career
**Q:** What jobs have Computer Science graduates obtained?

**Reference:** Software engineer, testing engineer, AI engineer, data engineer, business analyst, product owner, product development manager.

**Answer:** Computer Science graduates have obtained the following jobs:

- Software engineer
- Testing engineer
- AI engineer
- Data engineer
- Business analyst
- Product owner
- Product development manager

[CS_MajorHandbook.pdf p.4]

*Retrieved:* CS_MajorHandbook.pdf p.6 (0.71); CS_MajorHandbook.pdf p.5 (0.70); CS_MajorHandbook.pdf p.2 (0.64); CS_MajorHandbook.pdf p.4 (0.63); CS_MajorHandbook.pdf p.14 (0.62)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 16.9s

### Q18 · qwen3.5:9b · teaching_assessment
**Q:** How are students taught and assessed in the Computer Science major?

**Reference:** Active and collaborative learning; continuous formative assessment through discussion, in-class activities and applied learning, plus quizzes, exams, projects, presentations and the capstone.

**Answer:** Students in the Computer Science major are taught and assessed through active and collaborative learning, utilizing methods such as lectures, labs, group discussions, and applied learning projects [CS_MajorHandbook.pdf p.12]. Assessment combines summative methods like exams and programming tests with continuous formative assessment through in-class activities and discussions [CS_MajorHandbook.pdf p.12]. Specific teaching and learning methods vary by learning outcome, including reading, field trips, and capstone projects [CS_MajorHandbook.pdf p.12].

*Retrieved:* CS_MajorHandbook.pdf p.12 (0.77); CS_MajorHandbook.pdf p.12 (0.74); CS_MajorHandbook.pdf p.4 (0.73); CS_MajorHandbook.pdf p.4 (0.72); CS_MajorHandbook.pdf p.14 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 20.09s

### Q19 · qwen3.5:9b · program_requirements
**Q:** How many exploratory courses must students take, and how many can count toward the major?

**Reference:** 6 exploratory courses (24 credits); up to 2 courses (8 credits) can count toward the major.

**Answer:** Students must take 6 exploratory courses (24 credits), consisting of 2 courses from each of three categories: Arts and Humanities, Social Sciences, and STEM. Among these 6 courses, up to 2 courses (8 credits) can be counted toward the major [CS_MajorHandbook.pdf p.7].

*Retrieved:* CS_MajorHandbook.pdf p.7 (0.76); CS_MajorHandbook.pdf p.7 (0.68); CS_MajorHandbook.pdf p.6 (0.67); CS_MajorHandbook.pdf p.13 (0.64); CS_MajorHandbook.pdf p.11 (0.63)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 18.26s

### Q20 · qwen3.5:9b · ambiguous
**Q:** What degree is awarded after completing the degree requirements?

**Reference:** A B.S. in Computer Science. Note: the handbook's Degree Requirements section says 'Bachelor of Science in Applied Mathematics', an apparent copy-paste error that may mislead the model.

**Answer:** A Bachelor of Science in Applied Mathematics is awarded following the successful completion of the degree requirements. [CS_MajorHandbook.pdf p.6]

*Retrieved:* CS_MajorHandbook.pdf p.6 (0.66); CS_MajorHandbook.pdf p.2 (0.62); CS_MajorHandbook.pdf p.3 (0.61); CS_MajorHandbook.pdf p.6 (0.60); CS_MajorHandbook.pdf p.5 (0.59)  
*Retrieval hit:* True · *keyword score:* 0.0 · *latency:* 15.15s

### Q21 · qwen3.5:9b · out_of_scope
**Q:** What is the tuition fee for the Computer Science program?

**Reference:** Not stated in the handbook; the chatbot should say it cannot find the information.

**Answer:** I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.2 (0.68); CS_MajorHandbook.pdf p.4 (0.65); CS_MajorHandbook.pdf p.19 (0.64); CS_MajorHandbook.pdf p.14 (0.64); CS_MajorHandbook.pdf p.4 (0.64)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 13.78s

### Q22 · qwen3.5:9b · other
**Q:** Which universities' programs were used as references for the CS curriculum?

**Reference:** Stanford University, Carnegie Mellon University and Cornell University.

**Answer:** I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.2 (0.71); CS_MajorHandbook.pdf p.11 (0.69); CS_MajorHandbook.pdf p.14 (0.68); CS_MajorHandbook.pdf p.6 (0.68); CS_MajorHandbook.pdf p.7 (0.68)  
*Retrieval hit:* False · *keyword score:* 0.0 · *latency:* 15.11s

### Q23 · qwen3.5:9b · off_topic
**Q:** Who won the 2022 FIFA World Cup?

**Reference:** Unrelated to the handbook; the chatbot should say it cannot find the information.

**Answer:** I could not find this in the documents.

*Retrieved:* (none)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 2.24s

### Q24 · qwen3.5:9b · off_topic
**Q:** Write a Python function that reverses a string.

**Reference:** Unrelated to the handbook; in strict mode the chatbot should decline.

**Answer:** I could not find this in the documents.

*Retrieved:* (none)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 0.27s

### Q25 · qwen3.5:9b · follow_up
*Asked after:* Tell me about CS311 Advanced Deep Learning.

**Q:** What is its prerequisite?

**Reference:** CS313 Deep Learning for AI ("its" = CS311 from the previous turn).

**Answer:** The prerequisite for CS311 Advanced Deep Learning is CS313 [CS_MajorHandbook.pdf p.18].

*Retrieved:* CS_MajorHandbook.pdf p.18 (0.89); CS_MajorHandbook.pdf p.18 (0.82); CS_MajorHandbook.pdf p.18 (0.74); CS_MajorHandbook.pdf p.17 (0.72); CS_MajorHandbook.pdf p.13 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 16.71s

### Q26 · qwen3.5:9b · follow_up
*Asked after:* What are the prerequisites for CS 302 Algorithms & Theory of Computing?

**Q:** And how often is it offered?

**Reference:** Once a year ("it" = CS 302 from the previous turn).

**Answer:** CS302 is offered once a year [CS_MajorHandbook.pdf p.13].

*Retrieved:* CS_MajorHandbook.pdf p.17 (0.80); CS_MajorHandbook.pdf p.13 (0.74); CS_MajorHandbook.pdf p.17 (0.72); CS_MajorHandbook.pdf p.14 (0.72); CS_MajorHandbook.pdf p.12 (0.71)  
*Retrieval hit:* True · *keyword score:* 1.0 · *latency:* 15.61s

### Q27 · qwen3.5:9b · follow_up_off_topic
*Asked after:* What is the prerequisite for CS311 Advanced Deep Learning?

**Q:** Who won the 2022 FIFA World Cup?

**Reference:** Off-topic question asked right after a handbook question; the chatbot should still refuse.

**Answer:** I could not find this in the documents.

*Retrieved:* CS_MajorHandbook.pdf p.18 (0.71); CS_MajorHandbook.pdf p.18 (0.67); CS_MajorHandbook.pdf p.18 (0.63); CS_MajorHandbook.pdf p.15 (0.60); CS_MajorHandbook.pdf p.15 (0.60)  
*Retrieval hit:*  · *keyword score:*  · *latency:* 14.99s
