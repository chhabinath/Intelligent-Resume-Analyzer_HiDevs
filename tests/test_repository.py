from candidate_repository import CandidateRepository

repo = CandidateRepository()

print("Candidate Count:")
print(repo.count_candidates())

repo.close()