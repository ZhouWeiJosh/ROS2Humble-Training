# ROS2 Humble Training

This repository contains a structured series of exercises designed to help the team
learn **ROS 2 (Humble)** fundamentals in a consistent, reproducible way.


---

## Prerequisites

Before starting any exercises in this repository, **you must complete the setup steps**
outlined in the following Google Doc:

https://docs.google.com/document/d/1S7wsK-0SaU3Z1uF1xBy5d9fthQ_KXShjgsPyszLhCok/edit?usp=sharing

Specifically, complete the sections covering:
- Ubuntu 22.04 installation
- GitHub account setup and SSH keys
- ROS 2 Humble installation

If your environment is not set up correctly, you *will* encounter confusing errors later.
Do not skip this step.

---

## Repository Philosophy

- `main` branch contains **instructions only**
- Each exercise is completed in **its own branch**
- Your ROS 2 workspace lives **inside your exercise branch**
- Nothing experimental or incomplete should be committed to `main`

Think of `main` as the textbook, and your branches as the homework.

---

## GitHub Basics (Critical)

Version control is non-optional in robotics. You will be expected to:
- Create branches
- Commit incremental progress
- Push and pull changes
- Resolve conflicts

A solid beginner-friendly Git overview can be found here:
https://youtu.be/Ala6PHlYjmw?si=1gQsiJoMZakCsRcw

### How We Use Git in This Training

- `main`
  - Contains README files and written instructions
  - Should never contain a ROS 2 workspace

- `week*-name` branches
  - Contain your actual ROS 2 code
  - Example: `week1-Lawrence`, `week1-Jordan`

Typical workflow:
1. Checkout `main`
2. Create a new branch for the exercise
3. Do all work in that branch
4. Commit frequently
5. Push your branch to GitHub

---

## Common Git Commands

Check the status of your working directory:
```bash
git status
```
List all local branches:
```bash
git branch
```
Create and switch to a new branch for an exercise:
```bash
git checkout -b week1-<yourname>
```
Push your current branch to GitHub (first push sets upstream):
```bash
git push -u origin week1-<yourname>
```
Pull the latest changes from the remote branch you are tracking:
```bash
git pull
```
Fetch updates from the remote repository without modifying your working tree:
```bash
git fetch
```
Switch between existing branches:
```bash
git checkout main
```
