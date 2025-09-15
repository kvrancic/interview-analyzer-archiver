# Interview Analysis & Learning Document

Generated: 2025-09-15 11:02

## Summary

- **Total Questions:** 58
- **Technical Questions:** 32
- **Performance:**
  - ✅ Correct: 1
  - ⚠️ Partially Correct: 5
  - ❌ Incorrect: 26

---

## Game Theory

### Question 1

**Q:** The winner of these games then play each other in the final.

**Candidate:** Ok.

---

### Question 2

**Q:** The higher-ranked team will actually be a 75/25 favorite to win each game.

**Candidate:** Ok, so higher one has 75% of winning.

---

### Question 3

**Q:** So let’s play the game. You have four face-down cards in front of you. Are you—what are you going to do? You going to randomly pick one, or are you going to discard and take 25?

**Candidate:** Can just quick ask, do we do one turn of this game or until all cards are—

---

### Question 4

**Q:** So now let's think a bit more about the expected value of the game as a whole. So not given that first card is 30, but rather starting the game from scratch.

**Candidate:** Mmmhmm.

**Evaluation:** ❌ Incorrect

**Model Answer:** To calculate the expected value of the game, we need to consider all possible outcomes and their probabilities. This involves summing the product of each outcome's value and its probability, taking into account the initial card draw and subsequent decisions. The expected value represents the average outcome if the game were played many times.

**Note:** The candidate's answer "Mmmhmm" is not a substantive response and does not demonstrate any understanding of how to calculate the expected value of the game.

---

### Question 5

**Q:** So, yes, so very quickly what’s a lower bound—like what’s a very easy lower bound for the value of the game?

**Candidate:** Lower bound for the value of game is definitely… Hmm, that should be... 100?

---

### Question 6

**Q:** So I guess my question is, where do you think— in words—why do you think the game’s worth more than 100?

**Candidate:** What? Can you repeat?

---

### Question 7

**Q:** So intuitively, why is the game worth more than 100?

**Candidate:** Because of the cards worth 30 and 40 points. So—and because of them, they are larger than discarding—than the move of discarding—and 10 and 20 we can, let's say, replace them with a discard and get more value out of them. So that’s kind of intuition.

---

### Question 8

**Q:** What do you think the expected value of the game is if you pull 40 first?

**Candidate:** It should be a little bit larger, maybe about 112.5. Maybe something around that.

**Evaluation:** ❌ Incorrect

**Model Answer:** The expected value of this game is 100. This is calculated by multiplying the probability of winning (0.5) by the payout (200).

**Note:** The candidate's answer is incorrect because it does not reflect the correct calculation of the expected value for this game.

---

## General

### Question 1

**Q:** And underlying trades at 100.

**Candidate:** Ok.

---

### Question 2

**Q:** Yes, I believe that’s also a correct definition.

**Candidate:** Awesome.

---

### Question 3

**Q:** What do you think—so as a function of the underlying price, what do you think the delta of the 98 call looks like?

**Candidate:** The delta of 98 call… we are at how—expiration date?

**Evaluation:** ❌ Incorrect

**Model Answer:** The delta of a 98 call option increases as the underlying price rises above the strike price, approaching 1 as the underlying price moves significantly higher. Conversely, it decreases towards 0 as the underlying price falls below the strike price.

**Note:** The candidate's answer is incomplete as it fails to describe the relationship between the underlying price and the delta of the call option.

---

### Question 4

**Q:** Let’s say we’re one second away from expiring.

**Candidate:** One second… It's very close to one.

---

### Question 5

**Q:** So I mean, as a function of the—so if the underlying is 100, what’s the delta?

**Candidate:** Just to be clear, so strike price is 98, right?

**Evaluation:** ⚠️ Partially Correct

**Model Answer:** The delta of an option is the rate of change of the option's price with respect to a $1 change in the underlying asset's price. Without knowing the specific option (e.g., call/put, time to expiry, volatility), it's impossible to give a precise delta value, but it's typically between 0 and 1 for calls and -1 and 0 for puts.

**Note:** The candidate correctly identified the need for clarification on the strike price, which is a necessary input, but did not provide the actual delta or explain how it's calculated.

---

### Question 6

**Q:** Well, you tell me, can it be negative?

**Candidate:** Uhm... Not really.

---

### Question 7

**Q:** I’m just saying, so let’s say I’m one second before expiry.

**Candidate:** Ok.

**Evaluation:** ❌ Incorrect

**Model Answer:** At one second before expiry, a financial derivative would be valued based on its intrinsic value plus any remaining time value, which would be minimal. The intrinsic value is the immediate profit if exercised, and the time value reflects the possibility of future price movements.

**Note:** The candidate's answer is a simple acknowledgment and does not provide any technical information about the valuation of a derivative at that specific time.

---

### Question 8

**Q:** So what do you think happens to that profile as you move away from expiry?

**Candidate:** As I move away from expiry... What happens to the what? The delta or...?

**Evaluation:** ❌ Incorrect

**Model Answer:** As you move away from expiry, the implied volatility of an option generally decreases. This is because there is more time for the underlying asset's price to move significantly, making the option less sensitive to small price changes.

**Note:** The candidate did not provide an answer, instead asking for clarification, indicating they did not understand the question or the underlying concepts.

---

### Question 9

**Q:** No, I’m saying that so we found the case for one second before expiry.

**Candidate:** Ok.

**Evaluation:** ❌ Incorrect

**Model Answer:** The candidate's answer is a simple acknowledgment and does not provide any technical information or demonstrate understanding of the concept of "one second before expiry." A correct answer would explain the implications of this timing, such as potential race conditions or the need for proactive handling of expiring resources.

**Note:** The candidate's response is a non-committal acknowledgment and offers no technical insight or explanation.

---

### Question 10

**Q:** Now let’s say we are five years from expiry.

**Candidate:** Ok.

**Evaluation:** ❌ Incorrect

**Model Answer:** This is a very open-ended question. To provide a useful answer, I would need more context about what we are evaluating at five years from expiry. For example, are we discussing financial instruments, product lifecycles, or something else?

**Note:** The candidate's answer is too brief and doesn't acknowledge the ambiguity of the question, failing to prompt for necessary clarification.

---

### Question 11

**Q:** What do you think the delta as a function of the current underlying price looks like?

**Candidate:** Oh, the current underlying price… So, if it’s very close to the underlying price, and five years… I would say…

**Evaluation:** ❌ Incorrect

**Model Answer:** Delta as a function of the underlying price is typically an "S" shaped curve. It starts near zero for prices far below the strike, increases towards 0.5 as the price approaches the strike, and then approaches 1 for prices far above the strike.

**Note:** The candidate's answer is rambling and does not provide any relevant information about the shape of the delta function.

---

### Question 12

**Q:** Now let’s say I’m instead five years away from expiry.

**Candidate:** Ok.

**Evaluation:** ❌ Incorrect

**Model Answer:** If you are five years away from expiry, the value of the option would be significantly higher than if it were close to expiry. This is because there is more time for the underlying asset's price to move favorably, increasing the probability of the option expiring in-the-money. The time value component of the option's price would be substantial.

**Note:** The candidate's answer is too brief and provides no insight into the implications of being five years from expiry.

---

### Question 13

**Q:** Would you expect the delta to still be one?

**Candidate:** No, it should be definitely lower because a change today, let’s say, matters less than a change one second before. So one increase in one matters much less than an increase because it has time to move much more up or down.

**Evaluation:** ❌ Incorrect

**Model Answer:** The delta would still be one if the change being measured is a discrete event, like a single user action. However, if the question implies a rate of change or a continuous process, the delta would likely be lower due to the time factor mentioned.

**Note:** The candidate incorrectly assumes the delta is always a measure of time-decayed value, rather than a measure of change itself.

---

### Question 14

**Q:** Yes. Teams 1, 2, 3, and 4. And the structure of the tournament is essentially a semi-final where team 2 plays team 3 and team 1 plays team 4.

**Candidate:** Ok.

---

### Question 15

**Q:** The prize structure is that the winner gets 120 points, the runner-up gets 80 points, and the third- and fourth-place finishers get nothing.

**Candidate:** Ok, and the second, so when—aha, ok. The first one gets 120, the second one 80, and the third and fourth nothing?

---

### Question 16

**Q:** And feel free to talk through your calculation.

**Candidate:** Ok, so for team 1 to be—to get the first prize, team 1 needs to beat team number 4, and team number 1 needs to beat the winner of match between 2 and 3. But it doesn’t really matter which one, 2 or 3, win because team 1 has more skill, so it is favored to win. So basically to get number one prize it’s 75% times 75%, so that’s the chance of winning 120 points. And plus we need to calculate chance on winning the second prize, that’s 0.75 chance times 25% chance because team number 1 needs to win its first match then lose its second match.

---

### Question 17

**Q:** So that means essentially you have 95 points left to split between the two other teams.

**Candidate:** Ok.

---

### Question 18

**Q:** Because 82.5 plus 22.5 is 105.

**Candidate:** Ok.

---

### Question 19

**Q:** That makes sense to you?

**Candidate:** Yeah, yeah. Yes.

---

### Question 20

**Q:** But you do not get to see the card that you discarded.

**Candidate:** Ooh, I don’t get to see the card I discard. Ok, ok.

---

### Question 21

**Q:** Yes, you keep going until all the cards are discarded or turned over.

**Candidate:** Ok, so currently the expected value of me pulling—turning face up one card is… that is 100 divided by 4, so that’s 25. So yeah, the expected value of me turning up one card and discarding one card is currently exactly the same. But I think that maybe I will get more information if I turn one card face up.

---

### Question 22

**Q:** Logically, you would have no reason to keep cards after that, right?

**Candidate:** Yeah, yeah.

---

### Question 23

**Q:** So if you picked 30, you're saying you would just discard the last 3 cards?

**Candidate:** Yeah, yeah, actually yeah, because if I turn face up them, I will— in the end I will have total 70, and if I discard all three cards, I will have 75. So yeah, definitely, I’ll discard them, all of them, yeah.

---

### Question 24

**Q:** So that’s definitely better than turning over all the cards.

**Candidate:** Yeah, yes.

---

### Question 25

**Q:** Do you think you might be able to do better?

**Candidate:** Could I do better... No, because I don’t get any... Ok at first my intuition tells me that no, because I don’t have any intuition—because I don’t get any information when I discard a card, so the—

---

### Question 26

**Q:** No, I’m talking about rather than discarding the second card, can you do better than that if you pick the card instead?

**Candidate:** If I pick the—at what turn, first turn or second turn?

---

### Question 27

**Q:** Second turn. First card is a 30.

**Candidate:** Oh ok.

---

### Question 28

**Q:** Versus if you just discard the last three cards and actually you would only have 105. So this is better indeed.

**Candidate:** Yes.

---

### Question 29

**Q:** But yeah, very nice to speak with you. Yeah, thanks very much.

**Candidate:** Awesome, thank you.

---

## Options

### Question 1

**Q:** So let’s say I have the 98 strike call.

**Candidate:** Ok.

**Evaluation:** ❌ Incorrect

**Model Answer:** A 98 strike call option gives the holder the right, but not the obligation, to buy an underlying asset at a price of $98 per share. This option is "in the money" if the current market price of the underlying asset is above $98.

**Note:** The candidate's answer is a simple acknowledgement and provides no information about the meaning or implications of a 98 strike call.

---

### Question 2

**Q:** And we’re at the expiry date of the option.

**Candidate:** Ok.

**Evaluation:** ❌ Incorrect

**Model Answer:** At the expiry date of an option, the holder decides whether to exercise it based on whether it is "in the money." If it's in the money, they will exercise it to realize the profit; otherwise, they will let it expire worthless.

**Note:** The candidate's answer is a simple acknowledgment and provides no relevant information about what happens at the expiry date of an option.

---

### Question 3

**Q:** What’s the value of the option?

**Candidate:** Two.

**Evaluation:** ❌ Incorrect

**Model Answer:** The value of an option depends on several factors, including the underlying asset's price, the strike price, time to expiration, volatility, and interest rates. Without knowing these parameters, it's impossible to determine the option's value.

**Note:** The candidate provided a numerical answer without any context or justification, making it impossible to verify its correctness.

---

### Question 4

**Q:** So now let’s say I’m instead one year away from expiring. Would you say that the value of this option is more or less than two?

**Candidate:** More than two.

**Evaluation:** ✅ Correct

**Model Answer:** Yes, the value of the option would be more than two. As the expiration date approaches, the time value of the option decreases, but the intrinsic value (the difference between the stock price and the strike price) becomes more dominant. If the stock price is significantly above the strike price, the option's value will be higher than two.

**Note:** The candidate correctly identified that the option's value would be more than two, but their answer lacked the necessary reasoning to explain why.

---

### Question 5

**Q:** How would you compare the value of a one-year-out option versus a five-year-out option?

**Candidate:** Yeah, five-year is definitely more expensive because let’s say it has more time to go up.

**Evaluation:** ⚠️ Partially Correct

**Model Answer:** A five-year option is generally more valuable than a one-year option due to the longer time horizon, which increases the probability of favorable price movements and allows for more compounding of potential gains. This extended time value of money, along with reduced risk of expiring worthless before a significant price change, contributes to its higher premium.

**Note:** The candidate correctly identifies that the five-year option is more expensive due to more time, but the explanation is overly simplistic and lacks the nuance of probability and compounding.

---

### Question 6

**Q:** So, no, you don’t need to make a function, I’m just asking you, if the underlying is trading at 100 and the strike price is 98, what’s the delta of your option one second before expiring?

**Candidate:** Delta one second before my expiry... It should be... one second... to think about it... if it increases by one... it should be… it should be one.

**Evaluation:** ⚠️ Partially Correct

**Model Answer:** For an in-the-money call option one second before expiry, the delta will be very close to 1. For an in-the-money put option, the delta will be very close to -1.

**Note:** The candidate correctly identified that the delta would be close to 1 for a call option, but didn't consider the case of a put option or the nuance of "very close to" rather than exactly 1.

---

### Question 7

**Q:** It's essentially a step function, right, at the strike price.

**Candidate:** At the strike price, step function? What do you mean by step function? What is the domain of that function? Underlying asset, right?

**Evaluation:** ⚠️ Partially Correct

**Model Answer:** Yes, the payoff of a European call option is a step function. The domain is the price of the underlying asset, and the function is zero below the strike price and increases linearly above it.

**Note:** The candidate correctly identified the underlying asset as the domain but failed to elaborate on the function's behavior or confirm the step function concept.

---

### Question 8

**Q:** And if underlying is trading below the strike price, we kind of establish it’s delta zero, and if it trades above, it’s more or less delta one, right?

**Candidate:** Uhm… yeah, yeah, yeah.

**Evaluation:** ❌ Incorrect

**Model Answer:** While delta is influenced by the underlying's price relative to the strike, it's not a binary 0 or 1. Delta is a continuous measure that approaches 0 for deep out-of-the-money options and approaches 1 for deep in-the-money options, but it's also affected by time to expiration and volatility.

**Note:** The candidate's answer oversimplifies the concept of delta, presenting it as a binary state rather than a continuous variable.

---

### Question 9

**Q:** So essentially we have this shift in domain around the strike price.

**Candidate:** Yeah, I agree, I agree.

**Evaluation:** ❌ Incorrect

**Model Answer:** The statement "shift in domain around the strike price" is vague and doesn't convey a clear technical concept. A more precise explanation would involve discussing how the probability of an option expiring in-the-money changes as the underlying asset's price moves relative to the strike price.

**Note:** The candidate's agreement is insufficient as the original statement lacks technical clarity and doesn't demonstrate understanding.

---

### Question 10

**Q:** So we looked at the case where the underlying trades at 102 and the strike price is 100, right?

**Candidate:** Yeah, yeah, ok.

**Evaluation:** ❌ Incorrect

**Model Answer:** The question is asking for confirmation of a specific scenario. A correct answer would acknowledge the scenario presented and potentially offer a brief confirmation or elaboration.

**Note:** The candidate's answer is a non-committal "Yeah, yeah, ok" which doesn't confirm or deny understanding of the specific scenario presented.

---

### Question 11

**Q:** At one second before expiry, that’s a delta 1 option.

**Candidate:** Ok.

**Evaluation:** ⚠️ Partially Correct

**Model Answer:** A delta 1 option is an option whose delta is approximately 1. This typically occurs when the option is deep in the money and the underlying asset's price is significantly above the strike price.

**Note:** The candidate's answer is partially correct because while a delta of 1 is a key characteristic, the answer lacks the context of what that delta implies in terms of the option's moneyness.

---

### Question 12

**Q:** And again, underlying is 102 and my strike price is 100.

**Candidate:** Ok.

**Evaluation:** ❌ Incorrect

**Model Answer:** The candidate's answer is a confirmation of the provided information, but it doesn't demonstrate any understanding or analysis of the scenario. A correct answer would involve explaining the implications of these values, such as whether the option is in-the-money or out-of-the-money.

**Note:** The candidate simply acknowledged the numbers without providing any relevant financial analysis or interpretation.

---

### Question 13

**Q:** Now this game is going to be that I put the cards face down in front of you. And you, at every turn, have two options: you can choose to turn over a card, turn over a random card, and receive that value in dollars, or you can choose to discard a card and receive $25.

**Candidate:** Ok.

**Evaluation:** ❌ Incorrect

**Model Answer:** The optimal strategy depends on the distribution of card values. If the expected value of turning over a card is greater than $25, you should turn it over. Otherwise, you should discard it.

**Note:** The candidate's answer is simply "Ok," which does not address the strategic decision required by the question.

---

## Statistics

### Question 1

**Q:** So if every team is equally skilled, then what’s the expected value of each team?

**Candidate:** Expected value of each team is... one second… It should be 50.

**Evaluation:** ❌ Incorrect

**Model Answer:** If every team is equally skilled, then the expected value of each team is the average of all possible outcomes. Without knowing the specific outcomes or the number of teams, we cannot definitively state the expected value is 50.

**Note:** The candidate jumped to a specific number without any context or calculation, which is not a valid approach to determining expected value.

---

### Question 2

**Q:** So what’s the expected value—can you calculate for me the expected value of team 1?

**Candidate:** Expected value of team 1 is… ok, one second…

**Evaluation:** ❌ Incorrect

**Model Answer:** The expected value of team 1 is calculated by summing the products of each possible outcome's value and its probability. Without knowing the specific outcomes and their probabilities for team 1, a numerical answer cannot be provided.

**Note:** The candidate did not provide any calculation or attempt to define the necessary components for calculating expected value.

---

### Question 3

**Q:** I’m now going to tell you that the expected value of team 4 is 22.5.

**Candidate:** Ok.

**Evaluation:** ❌ Incorrect

**Model Answer:** The candidate's answer is a simple acknowledgment and does not demonstrate any understanding or calculation related to the provided expected value. A good answer would involve confirming the value and potentially asking for clarification or context.

**Note:** The candidate's response is a mere "Ok," which is insufficient as it provides no indication of understanding or engagement with the given information.

---

### Question 4

**Q:** You told me that already the immediate expected value of picking a card is 23.3 versus 25 of discarding right?

**Candidate:** Uh yes. Ok, maybe, maybe I can do better if I try to get to the 40 and then discard the rest. So let’s say I do a strategy where I turn face up until I found 40 and then discard the rest. So in one third of chances, I will—in the end I will have 40 plus 50—90 dollars. In one third chance I will have 15 plus 40—55 plus 25, that should be 80. And in one third chance I will... I will get 70. So yeah, actually yeah, this is better. This strategy is better. So expected value is 80 with this strategy.

**Evaluation:** ❌ Incorrect

**Model Answer:** The candidate's calculation for the expected value of the "stop at 40" strategy is incorrect. A correct analysis would involve considering all possible outcomes and their probabilities, leading to a different expected value.

**Note:** The candidate incorrectly calculated the expected value of their proposed strategy by misinterpreting the probabilities and outcomes of drawing cards.

---

## Trading

### Question 1

**Q:** So what's your market?

**Candidate:** 108.5 and 109.5.

**Evaluation:** ❌ Incorrect

**Model Answer:** My market is the range of prices at which a buyer is willing to purchase a security and a seller is willing to sell it. This is often referred to as the bid-ask spread.

**Note:** The candidate provided numerical values without context, which is not a definition of a market.

---

### Question 2

**Q:** So can you make me a market on the number of iPhones sold in America in 2024, in millions? And can you make it five million wide?

**Candidate:** Five million wide? Ok, so let’s say America has about… 300... Around 300 million people. So, and most of them has—have an iPhone. Let’s say around… 60… 50? 50? Around 50 million. So 47.5, 52.5. Let's do that.

**Evaluation:** ❌ Incorrect

**Model Answer:** A reasonable market size for iPhones sold in America in 2024, with a five million wide range, could be between 50 million and 55 million units. This accounts for a significant portion of the US population owning iPhones, considering upgrade cycles and new device adoption.

**Note:** The candidate misunderstood the question, providing a range around a single number rather than a market size estimate with a specified width.

---

### Question 3

**Q:** I buy it from you, what’s your next market?

**Candidate:** You buy from me, ok. So I will push it a little bit more. So let’s say 50... 51.5, 56.5.

**Evaluation:** ❌ Incorrect

**Model Answer:** The next market would be a different customer segment or geographical region that has a similar need for the product but is currently underserved. This expansion would leverage the existing product and customer base to achieve further growth.

**Note:** The candidate misinterpreted the question as a negotiation on price rather than a strategic question about market expansion.

---

### Question 4

**Q:** Uh yeah, so actually I did a trading internship when I was in university at another trading firm. But for me, the thing that pulled me away was, as a trader you are a little bit more into making kind of on-the-fly decisions and less about longer-term work. And one thing that from my background was appealing is just being able to work on more longer-term projects and thinking a little bit more deeply about problems. But that being said, I think at Da Vinci more than other trading firms, it's a little bit less clear the distinction between a quant researcher and a trader, and it's a quant trader. Because essentially there's no clear distinction in work. So I would bet even now I spend a lot of my time trading because I think it gives me better ideas and I can understand the market a bit better, and then traders also spend time doing research projects. So it’s not something I would worry too much about the distinction of, at least at Da Vinci. That's more or less why I chose.

**Candidate:** Ok, awesome.

**Evaluation:** ❌ Incorrect

**Model Answer:** The candidate's answer is "Ok, awesome." This is not an answer to the question asked. The question likely probed the candidate's reasoning for choosing a particular role or firm, and this response is a non-sequitur.

**Note:** The candidate provided a conversational filler instead of addressing the question, indicating a complete misunderstanding or failure to engage with the prompt.

---

