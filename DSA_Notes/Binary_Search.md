# Searching: Binary Search

- **Concept**: While Searching we need to have two things clear in our mind i.e 'What to Search(*TARGET*)' and 'Where to Search(*SEARCH SPACE*)'.
- **Ex**: 1. Target(*Word*) --> Seaching space could be (*Dictionary/Boooks/Newspaper*)
          2. Target(*Phone number*) --> Search Space (*Contacts*)

- **OBSERVATION**: If *search space* is ordered, seaching becomes easier.

# While doing Binary Search Why we land at mid only?
- If discarding n/3 part of the array there might be chances our target may be in the 2n/3 part, But if we discard n/2 part of the array we are surely discarding n/2 part of the array, in first case we are only discarding n/3 which means we still have 2n/3 of the array to travel.

- **NOTE**: Always we can discard N/2 (which is a better approach).
            Worst case we can only discard N/3 part of the array.

# When to apply Binary Search?
- After divinding search space into 2 parts, If we can somehow discard, half of search space, using some conditions then only we can apply BS.
- **NOTE**: If we cannot discard one half of Search space, we cannot apply BS.

## Problem solving approach is here
- https://scaler-production-new.s3.ap-southeast-1.amazonaws.com/attachments/attachments/000/016/847/original/Adv_Binary_Search_1_Copy__2_.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIDNNIRGHAQUQRWYA%2F20221014%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Date=20221014T114111Z&X-Amz-Expires=561600&X-Amz-SignedHeaders=host&X-Amz-Signature=671362699fcf414f7c7ab94f9d67536ab6b3ee1a8c3757a14e2db326e3e60dff




