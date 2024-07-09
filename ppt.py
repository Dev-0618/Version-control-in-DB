print("""		   [ THE ER DIAGRAM ]
###############################################################
#  +---------------------+             +---------------------+ #
#  |        User         |             |      GitCommit      | #
#  +---------------------+             +---------------------+ #
#  | PK: id              |             | PK: id              | #
#  |     username        | 1 ------- * |     commit_id       | #
#  |     password        |             |     branch          | #
#  |     role            |             |     message         | #
#  +---------------------+             |     date            | #
#               ^                      |     content         | #
#               |                      +---------------------+ #
#               |					       #
#               |					       #
#             Manages					       #
################################################################
""")


print(r"""
[ USER INTERFACE (CLI) ]
  |  
  |----> [ Authentication & Authorization ]""", input())
print(r"""  |			 |
  |   			 V
  |             ###################### 
  |		#+------------------+#
  |		#| User Operations  |#
  |		#| +--------------+ |#
  |		#| | View Users   | |#
  |		#| | Add User     | |#
  |		#| | Delete User  | |#
  |		#| | Update User  | |#
  |		#| +--------------+ |#
  |		#+------------------+#
  |             ######################""", input())
print(r"""  |               |
  V               V
+------------------------+
|   Initialize Databases |
|   |                    |
|   v                    |
|  users.db -------------+----> User Operations
|  {user}_git_commits.db |    Git Commit Operations
+------------------------+""", input())

print(r"""     |
     V
   Utility Functions (clear_screen, print_box, loading_animation)""", input())

print(r"""     |
     V
   User Interaction Loop""", input())
print(r"""	    |
            V
###########################
#+-----------------------+#
#| Git Commit Operations |#
#+-----------------------+#
#|  +-----------------+  |#
#|  | Fetch & Save    |  |#
#|  | Git Commit File |  |#
#|  | Update Commit   |  |#
#|  | Delete Commit   |  |#
#|  | Search Commits  |  |#
#|  +-----------------+  |#
#+-----------------------+#
###########################""", input())
print(r"""     |
     V
 [ TERMINATION ]

""", input())

