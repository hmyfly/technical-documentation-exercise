# Part 4: Reflections on Technical Documentation Practice

## On what makes documentation work

Good documentation is not measured by its completeness — it is measured by whether it enables the reader to do what they came to do. A page that covers every parameter exhaustively but buries the common case in the middle fails the developer who just needs to send their first message. A page that answers the most common question immediately, then layers in detail for those who need it, does its job even if it omits edge cases that belong elsewhere.

This means documentation is fundamentally an exercise in understanding users. The questions that matter are not "What does this parameter do?" but "What is the developer trying to accomplish when they land on this page, and what is the minimum they need to know to accomplish it?" Those are product questions, not writing questions. The best documentation contributors I have seen treat writing as the last step — the first step is user research: reading support tickets, watching users work through tutorials, auditing search queries, and sitting with the question of who exactly is going to read this.

## On the relationship between documentation and trust

For an API company, documentation is not just a support resource — it is a trust signal. A developer encountering Anthropic's API for the first time is evaluating not just whether the API does what they need, but whether they can rely on the documentation to be accurate when things go wrong at 2am before a launch. Inaccurate examples, stale parameter descriptions, and vague error guidance are not just inconveniences; they are reasons to choose a different API.

This is why I believe documentation quality has to be a shared responsibility and a process discipline, not just a talent discipline. A brilliant writer who produces accurate documentation at launch but has no mechanism to update it when the API changes is less valuable than a good writer embedded in a process that ensures every behavior change triggers a documentation review. Accuracy at publication is table stakes. Accuracy over time is the hard part, and it requires systems: ownership, review cycles, and a culture that treats "update the docs" as part of the definition of done for any feature change.

## On the technical documentation role specifically

The role of a technical documentation engineer at a company like Anthropic sits at an interesting intersection. The audience is technical — developers who will quickly notice if an example does not run, if a parameter description is imprecise, or if a guide omits the error case that always trips people up. But the skill is not purely technical: it is the ability to hold the developer's perspective while also understanding the system deeply enough to explain it accurately.

What I find most interesting about this role is that the leverage is asymmetric. A single well-written how-to guide, seen by thousands of developers, can reduce support load, improve integration success rates, and increase confidence in the product — all at once. A single inaccurate example, equally visible, can generate confusion across the same audience. This asymmetry is what makes documentation work both high-stakes and highly rewarding. The feedback loop is slow compared to software engineering, but the impact is broad and durable.

I also believe the role is evolving. As AI-assisted development becomes more common, documentation will be consumed not just by human developers but by language models being used as coding assistants. Documentation that is precise, structured, and unambiguous is not just good for human readers — it is better training signal and better context for AI tools helping developers use the API. This is a genuinely new dimension of quality that I think is worth taking seriously.
