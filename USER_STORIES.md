# User Stories - Café Order Management Prototype

This document contains the user stories for the café ordering prototype, covering both the Customer and Staff personas. 
*Note: Priority levels are defined as Must-Have, Should-Have, or Could-Have.*

## Customer Stories

### Story 1: Menu Browsing
**Priority:** Must-Have
**Story:** As a customer, I want to view the café menu on my phone so that I can decide what to order before I arrive.
**Acceptance Criteria:**
1. **Success:** Given the app is open, when I navigate to the menu, then I see a list of available items with their prices.
2. **Edge Case:** Given an item is sold out, when I view the menu, then that item is visibly marked as "Sold Out" or hidden and cannot be selected.

### Story 2: Order Submission
**Priority:** Must-Have
**Story:** As a customer, I want to submit my order digitally so that I don't have to wait in a long line to order at the register.
**Acceptance Criteria:**
1. **Success:** Given I have items in my cart, when I click "Submit Order," then the order is sent to the staff dashboard and I receive an order number.
2. **Error Case:** Given I have an empty cart, when I try to click "Submit Order," then the button is disabled and an error message says "Your cart is empty."

### Story 3: Check Order Status
**Priority:** Should-Have
**Story:** As a customer, I want to check the status of my order on my phone so that I know exactly when my food will be ready for pickup.
**Acceptance Criteria:**
1. **Success:** Given my order is placed, when the kitchen updates the status to "Preparing," then my app screen automatically updates to show "Preparing."
2. **Edge Case:** Given the system loses connection, when I try to refresh the page, then it shows a "Last updated at [Time]" message so I know the data might be slightly delayed.

### Story 4: Estimated Wait Time
**Priority:** Could-Have
**Story:** As a customer, I want to see an estimated wait time when I place my order so that I can manage my lunch break better.
**Acceptance Criteria:**
1. **Success:** Given I submit an order, when the order is confirmed, then I see an estimated time (e.g., "Ready in 10-15 mins").
2. **Edge Case:** Given the café is extremely busy (high volume), when I place an order, then the system adds a warning that wait times are longer than usual.

### Story 5: Cart Management
**Priority:** Should-Have
**Story:** As a customer, I want to clear my cart before ordering so that I can change my mind without starting over.
**Acceptance Criteria:**
1. **Success:** Given I have items in my cart, when I click "Clear Cart," then all items are removed.
2. **Time Constraint:** Given I clicked "Clear Cart," when 5 seconds pass without me undoing the action, then the cart remains empty permanently.

---

## Staff Stories

### Story 6: Unified Dashboard
**Priority:** Must-Have
**Story:** As a staff member, I want to view all incoming orders on a single dashboard so that I don't miss any orders from different channels.
**Acceptance Criteria:**
1. **Success:** Given a new order is submitted, when I look at the dashboard, then the new order appears at the top of the list instantly.
2. **Empty Field:** Given there are no active orders, when I look at the dashboard, then I see a message saying "No active orders" rather than a blank screen.

### Story 7: Update Order Status
**Priority:** Must-Have
**Story:** As a kitchen staff member, I want to move an order to the next status (Received -> Preparing -> Ready) so that customers know when their food is ready.
**Acceptance Criteria:**
1. **Success:** Given an order is received, when I click "Start Preparing," then it shows as "Preparing" on the kitchen board and the customer's screen.
2. **Wrong Role:** Given a customer is logged into their app, when they try to access the staff dashboard URL, then they are blocked with an "Access Denied" error.

### Story 8: Status Sequence Rules
**Priority:** Should-Have
**Story:** As a staff member, I want the system to prevent me from moving an order to "Ready" if it hasn't been marked "Preparing" first so that we don't skip steps and confuse the kitchen.
**Acceptance Criteria:**
1. **Success:** Given an order is "Received," when I try to click "Ready," then the button is disabled.
2. **Time Constraint:** Given an order has been in "Preparing" for over 15 minutes, when I look at the board, then the order card turns red to warn me it's taking too long.

---

## Assignment Questions

**1. Which story did you split into smaller stories, and why?**
I split the general "Customer Order Tracking" idea into Story 2 (Submitting the order) and Story 3 (Checking the status). I did this because submitting an order is a Must-Have core feature for the app to function, while checking the status on a phone is more of a Should-Have convenience. Combining them made the story too big to test efficiently.

**2. Which story was hardest to write acceptance criteria for? What made it hard?**
Story 4 (Estimated wait time) was the hardest. It was difficult to write clear criteria because the estimated time is an automated calculation based on kitchen volume. It is hard to test objectively because the number changes dynamically, making it difficult to write a strict "Given/When/Then" rule for a static prototype.