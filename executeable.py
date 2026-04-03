
# Create the complete working web application as a single file

complete_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A. James Art | Artist Accounting System</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary-black: #0a0a0a;
            --primary-white: #ffffff;
            --accent-gray: #2a2a2a;
            --light-gray: #f5f5f5;
            --border-gray: #e0e0e0;
            --success-green: #10b981;
            --warning-orange: #f59e0b;
            --danger-red: #ef4444;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Inter', sans-serif; background: var(--light-gray); color: var(--primary-black); line-height: 1.6; }
        
        /* Login Screen */
        .login-container {
            display: flex; justify-content: center; align-items: center; min-height: 100vh;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 50%, #2a2a2a 100%);
            position: relative; overflow: hidden;
        }
        .login-box {
            background: rgba(255,255,255,0.95); padding: 3rem; border-radius: 20px;
            box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5); width: 100%; max-width: 450px;
            z-index: 10; position: relative;
        }
        .logo-section { text-align: center; margin-bottom: 2rem; }
        .logo-text { font-family: 'Playfair Display', serif; font-size: 2rem; font-weight: 700; }
        .logo-text span { font-weight: 400; font-style: italic; }
        .tagline { color: #666; font-size: 0.9rem; margin-top: 0.5rem; }
        .form-group { margin-bottom: 1.5rem; }
        .form-group label { display: block; margin-bottom: 0.5rem; font-weight: 500; font-size: 0.9rem; }
        .input-wrapper { position: relative; }
        .input-wrapper i { position: absolute; left: 1rem; top: 50%; transform: translateY(-50%); color: #999; }
        .form-control {
            width: 100%; padding: 1rem 1rem 1rem 3rem; border: 2px solid var(--border-gray);
            border-radius: 12px; font-size: 1rem; transition: all 0.3s ease;
        }
        .form-control:focus { outline: none; border-color: var(--primary-black); box-shadow: 0 0 0 3px rgba(0,0,0,0.1); }
        .btn {
            width: 100%; padding: 1rem; border: none; border-radius: 12px; font-size: 1rem;
            font-weight: 600; cursor: pointer; transition: all 0.3s ease; font-family: 'Inter', sans-serif;
        }
        .btn-primary { background: var(--primary-black); color: var(--primary-white); }
        .btn-primary:hover { background: var(--accent-gray); transform: translateY(-2px); }
        .btn-secondary { background: transparent; color: var(--primary-black); border: 2px solid var(--primary-black); margin-top: 1rem; }
        .btn-secondary:hover { background: var(--primary-black); color: var(--primary-white); }
        .error-message { color: var(--danger-red); font-size: 0.9rem; margin-top: 0.5rem; display: none; }
        .success-message { color: var(--success-green); font-size: 0.9rem; margin-top: 0.5rem; display: none; }
        
        /* Dashboard */
        .dashboard { display: none; min-height: 100vh; }
        .sidebar {
            position: fixed; left: 0; top: 0; width: 280px; height: 100vh;
            background: var(--primary-black); color: var(--primary-white);
            padding: 2rem; overflow-y: auto; z-index: 1000;
        }
        .sidebar-header { margin-bottom: 3rem; padding-bottom: 2rem; border-bottom: 1px solid rgba(255,255,255,0.1); }
        .sidebar-logo { font-family: 'Playfair Display', serif; font-size: 1.5rem; margin-bottom: 0.5rem; }
        .user-info { font-size: 0.85rem; opacity: 0.7; display: flex; align-items: center; gap: 0.5rem; }
        .nav-menu { list-style: none; }
        .nav-item { margin-bottom: 0.5rem; }
        .nav-link {
            display: flex; align-items: center; gap: 1rem; padding: 1rem;
            color: rgba(255,255,255,0.7); text-decoration: none; border-radius: 12px;
            transition: all 0.3s ease; cursor: pointer;
        }
        .nav-link:hover, .nav-link.active { background: rgba(255,255,255,0.1); color: var(--primary-white); }
        .nav-link i { width: 24px; text-align: center; }
        .logout-btn {
            position: absolute; bottom: 2rem; left: 2rem; right: 2rem; padding: 1rem;
            background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2);
            color: var(--primary-white); border-radius: 12px; cursor: pointer;
            display: flex; align-items: center; justify-content: center; gap: 0.5rem;
        }
        .main-content { margin-left: 280px; padding: 2rem; min-height: 100vh; }
        .page-header { margin-bottom: 2rem; }
        .page-title { font-family: 'Playfair Display', serif; font-size: 2.5rem; margin-bottom: 0.5rem; }
        .page-subtitle { color: #666; }
        
        /* Stats */
        .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin-bottom: 2rem; }
        .stat-card { background: var(--primary-white); padding: 1.5rem; border-radius: 16px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
        .stat-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
        .stat-label { font-size: 0.9rem; color: #666; font-weight: 500; }
        .stat-icon { width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; }
        .stat-icon.revenue { background: rgba(16,185,129,0.1); color: var(--success-green); }
        .stat-icon.pending { background: rgba(245,158,11,0.1); color: var(--warning-orange); }
        .stat-icon.projects { background: rgba(99,102,241,0.1); color: #6366f1; }
        .stat-icon.expenses { background: rgba(239,68,68,0.1); color: var(--danger-red); }
        .stat-value { font-size: 2rem; font-weight: 700; margin-bottom: 0.25rem; }
        .stat-change { font-size: 0.85rem; color: var(--success-green); }
        
        /* Content Sections */
        .content-section { display: none; animation: fadeIn 0.3s ease; }
        .content-section.active { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        
        /* Tables */
        .table-container { background: var(--primary-white); border-radius: 16px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
        .table-header { padding: 1.5rem; border-bottom: 1px solid var(--border-gray); display: flex; justify-content: space-between; align-items: center; }
        .table-title { font-family: 'Playfair Display', serif; font-size: 1.5rem; }
        .btn-add { background: var(--primary-black); color: var(--primary-white); border: none; padding: 0.75rem 1.5rem; border-radius: 10px; cursor: pointer; display: flex; align-items: center; gap: 0.5rem; font-weight: 500; }
        .data-table { width: 100%; border-collapse: collapse; }
        .data-table th { background: var(--light-gray); padding: 1rem; text-align: left; font-weight: 600; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.5px; color: #666; }
        .data-table td { padding: 1rem; border-bottom: 1px solid var(--border-gray); }
        .data-table tr:hover { background: rgba(0,0,0,0.02); }
        .status-badge { padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.85rem; font-weight: 500; }
        .status-completed, .status-available { background: rgba(16,185,129,0.1); color: var(--success-green); }
        .status-progress, .status-in-progress { background: rgba(245,158,11,0.1); color: var(--warning-orange); }
        .status-pending, .status-scheduled { background: rgba(99,102,241,0.1); color: #6366f1; }
        
        /* Modal */
        .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 2000; justify-content: center; align-items: center; backdrop-filter: blur(5px); }
        .modal.active { display: flex; }
        .modal-content { background: var(--primary-white); border-radius: 20px; width: 90%; max-width: 600px; max-height: 90vh; overflow-y: auto; }
        .modal-header { padding: 1.5rem; border-bottom: 1px solid var(--border-gray); display: flex; justify-content: space-between; align-items: center; }
        .modal-title { font-family: 'Playfair Display', serif; font-size: 1.5rem; }
        .modal-close { background: none; border: none; font-size: 1.5rem; cursor: pointer; color: #666; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; }
        .modal-close:hover { background: var(--light-gray); }
        .modal-body { padding: 1.5rem; }
        .modal-footer { padding: 1.5rem; border-top: 1px solid var(--border-gray); display: flex; gap: 1rem; justify-content: flex-end; }
        .form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
        .form-group { margin-bottom: 1rem; }
        .form-group.full-width { grid-column: 1 / -1; }
        .btn-save { background: var(--primary-black); color: var(--primary-white); border: none; padding: 0.75rem 2rem; border-radius: 10px; cursor: pointer; font-weight: 600; }
        .btn-cancel { background: transparent; color: #666; border: 2px solid var(--border-gray); padding: 0.75rem 2rem; border-radius: 10px; cursor: pointer; font-weight: 600; }
        
        /* Action Buttons */
        .action-btns { display: flex; gap: 0.5rem; }
        .btn-icon { width: 32px; height: 32px; border: none; border-radius: 8px; cursor: pointer; display: flex; align-items: center; justify-content: center; }
        .btn-edit { background: rgba(99,102,241,0.1); color: #6366f1; }
        .btn-edit:hover { background: #6366f1; color: white; }
        .btn-delete { background: rgba(239,68,68,0.1); color: var(--danger-red); }
        .btn-delete:hover { background: var(--danger-red); color: white; }
        
        /* Gallery */
        .gallery-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.5rem; }
        .artwork-card { background: var(--primary-white); border-radius: 16px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
        .artwork-image { width: 100%; height: 200px; background: linear-gradient(135deg, #e0e0e0 0%, #f0f0f0 100%); display: flex; align-items: center; justify-content: center; font-size: 3rem; color: #ccc; }
        .artwork-info { padding: 1.5rem; }
        .artwork-title { font-family: 'Playfair Display', serif; font-size: 1.25rem; margin-bottom: 0.5rem; }
        .artwork-meta { color: #666; font-size: 0.9rem; margin-bottom: 1rem; }
        
        /* Toast */
        .toast-container { position: fixed; top: 2rem; right: 2rem; z-index: 3000; }
        .toast { background: var(--primary-white); padding: 1rem 1.5rem; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem; animation: slideIn 0.3s ease; min-width: 300px; }
        @keyframes slideIn { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
        .toast.success { border-left: 4px solid var(--success-green); }
        .toast.error { border-left: 4px solid var(--danger-red); }
        
        /* Loading */
        .loading { display: inline-block; width: 20px; height: 20px; border: 3px solid rgba(255,255,255,0.3); border-radius: 50%; border-top-color: white; animation: spin 1s ease-in-out infinite; }
        @keyframes spin { to { transform: rotate(360deg); } }
        
        /* Empty State */
        .empty-state { text-align: center; padding: 4rem 2rem; }
        .empty-state i { font-size: 4rem; color: #ddd; margin-bottom: 1rem; display: block; }
        .empty-state h3 { font-family: 'Playfair Display', serif; margin-bottom: 0.5rem; }
        .empty-state p { color: #666; margin-bottom: 1.5rem; }
        
        /* Pricing */
        .pricing-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; }
        .pricing-card { background: var(--primary-white); border-radius: 16px; padding: 1.5rem; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
        .pricing-header { margin-bottom: 1rem; padding-bottom: 1rem; border-bottom: 1px solid var(--border-gray); }
        .pricing-title { font-family: 'Playfair Display', serif; font-size: 1.25rem; }
        .pricing-amount { font-size: 2rem; font-weight: 700; }
        .pricing-note { font-size: 0.85rem; color: #666; margin-top: 0.5rem; }
        
        @media (max-width: 768px) {
            .sidebar { transform: translateX(-100%); transition: transform 0.3s ease; }
            .main-content { margin-left: 0; }
            .form-row { grid-template-columns: 1fr; }
            .stats-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <!-- Login Screen -->
    <div id="loginScreen" class="login-container">
        <div class="login-box">
            <div class="logo-section">
                <div style="font-size: 4rem; margin-bottom: 1rem;">🎨</div>
                <div class="logo-text">A. James <span>Art</span></div>
                <div class="tagline">Artist Accounting & Management System</div>
            </div>

            <div id="loginForm">
                <div class="form-group">
                    <label>Email Address</label>
                    <div class="input-wrapper">
                        <i class="fas fa-envelope"></i>
                        <input type="email" id="loginEmail" class="form-control" placeholder="your@email.com">
                    </div>
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <div class="input-wrapper">
                        <i class="fas fa-lock"></i>
                        <input type="password" id="loginPassword" class="form-control" placeholder="••••••••">
                    </div>
                </div>
                <div id="loginError" class="error-message"></div>
                <button onclick="login()" class="btn btn-primary" id="loginBtn">
                    <span id="loginText">Sign In</span>
                </button>
                <button onclick="showRegister()" class="btn btn-secondary">Create New Account</button>
            </div>

            <div id="registerForm" style="display: none;">
                <div class="form-group">
                    <label>Full Name</label>
                    <div class="input-wrapper">
                        <i class="fas fa-user"></i>
                        <input type="text" id="regName" class="form-control" placeholder="A. James">
                    </div>
                </div>
                <div class="form-group">
                    <label>Email Address</label>
                    <div class="input-wrapper">
                        <i class="fas fa-envelope"></i>
                        <input type="email" id="regEmail" class="form-control" placeholder="your@email.com">
                    </div>
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <div class="input-wrapper">
                        <i class="fas fa-lock"></i>
                        <input type="password" id="regPassword" class="form-control" placeholder="Min 6 characters">
                    </div>
                </div>
                <div id="registerError" class="error-message"></div>
                <div id="registerSuccess" class="success-message"></div>
                <button onclick="register()" class="btn btn-primary" id="registerBtn">
                    <span id="registerText">Create Account</span>
                </button>
                <button onclick="showLogin()" class="btn btn-secondary">Back to Sign In</button>
            </div>
        </div>
    </div>

    <!-- Dashboard -->
    <div id="dashboard" class="dashboard">
        <aside class="sidebar">
            <div class="sidebar-header">
                <div class="sidebar-logo">A. James Art</div>
                <div class="user-info">
                    <i class="fas fa-user-circle"></i>
                    <span id="userEmail">artist@ajames.com</span>
                </div>
            </div>
            <nav>
                <ul class="nav-menu">
                    <li class="nav-item"><a class="nav-link active" onclick="showSection('dashboard-home')"><i class="fas fa-home"></i><span>Dashboard</span></a></li>
                    <li class="nav-item"><a class="nav-link" onclick="showSection('commissions')"><i class="fas fa-palette"></i><span>Commissions</span></a></li>
                    <li class="nav-item"><a class="nav-link" onclick="showSection('expenses')"><i class="fas fa-receipt"></i><span>Expenses</span></a></li>
                    <li class="nav-item"><a class="nav-link" onclick="showSection('inventory')"><i class="fas fa-images"></i><span>Art Inventory</span></a></li>
                    <li class="nav-item"><a class="nav-link" onclick="showSection('clients')"><i class="fas fa-users"></i><span>Clients</span></a></li>
                    <li class="nav-item"><a class="nav-link" onclick="showSection('pricing')"><i class="fas fa-tags"></i><span>Pricing Guide</span></a></li>
                </ul>
            </nav>
            <button onclick="logout()" class="logout-btn"><i class="fas fa-sign-out-alt"></i><span>Logout</span></button>
        </aside>

        <main class="main-content">
            <!-- Dashboard Home -->
            <div id="dashboard-home" class="content-section active">
                <div class="page-header">
                    <h1 class="page-title">Dashboard Overview</h1>
                    <p class="page-subtitle">Welcome back, A. James. Here's your business at a glance.</p>
                </div>
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-header">
                            <span class="stat-label">Total Revenue (YTD)</span>
                            <div class="stat-icon revenue"><i class="fas fa-naira-sign"></i></div>
                        </div>
                        <div class="stat-value" id="totalRevenue">₦0</div>
                        <div class="stat-change"><i class="fas fa-arrow-up"></i> From commissions</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-header">
                            <span class="stat-label">Outstanding Payments</span>
                            <div class="stat-icon pending"><i class="fas fa-clock"></i></div>
                        </div>
                        <div class="stat-value" id="outstandingPayments">₦0</div>
                        <div class="stat-change"><i class="fas fa-exclamation-circle"></i> Pending balances</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-header">
                            <span class="stat-label">Active Commissions</span>
                            <div class="stat-icon projects"><i class="fas fa-paint-brush"></i></div>
                        </div>
                        <div class="stat-value" id="activeCommissions">0</div>
                        <div class="stat-change"><i class="fas fa-arrow-up"></i> In progress</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-header">
                            <span class="stat-label">Total Expenses</span>
                            <div class="stat-icon expenses"><i class="fas fa-wallet"></i></div>
                        </div>
                        <div class="stat-value" id="totalExpenses">₦0</div>
                        <div class="stat-change" style="color: var(--danger-red);"><i class="fas fa-arrow-down"></i> Deductible</div>
                    </div>
                </div>
                <div class="table-container" style="margin-top: 2rem;">
                    <div class="table-header">
                        <h3 class="table-title">Recent Commissions</h3>
                        <button onclick="openModal('commission')" class="btn-add"><i class="fas fa-plus"></i> New Commission</button>
                    </div>
                    <table class="data-table">
                        <thead><tr><th>Client</th><th>Artwork</th><th>Amount</th><th>Status</th><th>Due Date</th></tr></thead>
                        <tbody id="recentCommissionsTable"></tbody>
                    </table>
                </div>
            </div>

            <!-- Commissions -->
            <div id="commissions" class="content-section">
                <div class="page-header">
                    <h1 class="page-title">Commission Tracker</h1>
                    <p class="page-subtitle">Manage all your client commissions and projects.</p>
                </div>
                <div class="table-container">
                    <div class="table-header">
                        <h3 class="table-title">All Commissions</h3>
                        <button onclick="openModal('commission')" class="btn-add"><i class="fas fa-plus"></i> Add Commission</button>
                    </div>
                    <table class="data-table">
                        <thead><tr><th>ID</th><th>Client</th><th>Artwork Type</th><th>Medium</th><th>Total</th><th>Deposit</th><th>Balance</th><th>Status</th><th>Actions</th></tr></thead>
                        <tbody id="commissionsTable"></tbody>
                    </table>
                </div>
            </div>

            <!-- Expenses -->
            <div id="expenses" class="content-section">
                <div class="page-header">
                    <h1 class="page-title">Expense Tracker</h1>
                    <p class="page-subtitle">Track all your business expenses and art supplies.</p>
                </div>
                <div class="table-container">
                    <div class="table-header">
                        <h3 class="table-title">All Expenses</h3>
                        <button onclick="openModal('expense')" class="btn-add"><i class="fas fa-plus"></i> Add Expense</button>
                    </div>
                    <table class="data-table">
                        <thead><tr><th>Date</th><th>Category</th><th>Description</th><th>Vendor</th><th>Amount</th><th>Receipt</th><th>Actions</th></tr></thead>
                        <tbody id="expensesTable"></tbody>
                    </table>
                </div>
            </div>

            <!-- Inventory -->
            <div id="inventory" class="content-section">
                <div class="page-header">
                    <h1 class="page-title">Art Inventory</h1>
                    <p class="page-subtitle">Manage your available artworks and gallery pieces.</p>
                </div>
                <div style="margin-bottom: 2rem;">
                    <button onclick="openModal('artwork')" class="btn-add"><i class="fas fa-plus"></i> Add Artwork</button>
                </div>
                <div class="gallery-grid" id="inventoryGrid"></div>
            </div>

            <!-- Clients -->
            <div id="clients" class="content-section">
                <div class="page-header">
                    <h1 class="page-title">Client Database</h1>
                    <p class="page-subtitle">Manage your client relationships and contact information.</p>
                </div>
                <div class="table-container">
                    <div class="table-header">
                        <h3 class="table-title">All Clients</h3>
                        <button onclick="openModal('client')" class="btn-add"><i class="fas fa-plus"></i> Add Client</button>
                    </div>
                    <table class="data-table">
                        <thead><tr><th>Client Name</th><th>Type</th><th>Contact</th><th>Total Spent</th><th>Commissions</th><th>Rating</th><th>Actions</th></tr></thead>
                        <tbody id="clientsTable"></tbody>
                    </table>
                </div>
            </div>

            <!-- Pricing -->
            <div id="pricing" class="content-section">
                <div class="page-header">
                    <h1 class="page-title">Pricing Guide</h1>
                    <p class="page-subtitle">Standardized pricing for your art services.</p>
                </div>
                <div class="pricing-grid" id="pricingGrid"></div>
            </div>
        </main>
    </div>

    <!-- Modal -->
    <div id="dataModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3 class="modal-title" id="modalTitle">Add New</h3>
                <button onclick="closeModal()" class="modal-close"><i class="fas fa-times"></i></button>
            </div>
            <div class="modal-body" id="modalBody"></div>
            <div class="modal-footer">
                <button onclick="closeModal()" class="btn-cancel">Cancel</button>
                <button onclick="saveData()" class="btn-save" id="saveBtn">Save</button>
            </div>
        </div>
    </div>

    <div class="toast-container" id="toastContainer"></div>

    <script>
        // Data Store
        const DataStore = {
            get(key) { const data = localStorage.getItem(`ajames_${key}`); return data ? JSON.parse(data) : []; },
            set(key, value) { localStorage.setItem(`ajames_${key}`, JSON.stringify(value)); },
            init() {
                if (!localStorage.getItem('ajames_initialized')) {
                    this.set('commissions', [
                        { id: 'COM-2024-001', client: 'Mrs. Adebayo', contact: '+234 801 234 5678', artworkType: 'Hyperrealistic Portrait', medium: 'Charcoal & Graphite', size: '16x20', status: 'Completed', price: 75000, deposit: 75000, balance: 0, dueDate: '2024-02-15', completionDate: '2024-02-10', paymentStatus: 'Fully Paid' },
                        { id: 'COM-2024-002', client: 'Mr. Okonkwo', contact: '+234 802 345 6789', artworkType: 'Family Portrait', medium: 'Oil on Canvas', size: '24x36', status: 'In Progress', price: 150000, deposit: 75000, balance: 75000, dueDate: '2024-04-15', completionDate: '', paymentStatus: '50% Paid' }
                    ]);
                    this.set('expenses', [
                        { id: 'EXP-001', date: '2024-01-05', category: 'Art Supplies', description: 'Faber-Castell Pencils Set', vendor: 'Art World Nigeria', amount: 25000, paymentMethod: 'Bank Transfer', receipt: 'RCP-001', deductible: true },
                        { id: 'EXP-002', date: '2024-01-20', category: 'Art Supplies', description: 'Winsor & Newton Oil Paints', vendor: 'The Art Shop Lagos', amount: 45000, paymentMethod: 'Cash', receipt: 'RCP-002', deductible: true }
                    ]);
                    this.set('inventory', [
                        { id: 'ART-001', title: 'Eyes of Lagos', medium: 'Charcoal', size: '18x24', year: 2023, status: 'Available', price: 95000, location: 'Studio' },
                        { id: 'ART-002', title: 'Silent Strength', medium: 'Graphite', size: '14x17', year: 2024, status: 'Available', price: 65000, location: 'Studio' }
                    ]);
                    this.set('clients', [
                        { id: 'CLI-001', name: 'Mrs. Adebayo', type: 'Individual', contact: '+234 801 234 5678', email: 'adebayo@email.com', totalSpent: 75000, commissionCount: 1, rating: '★★★★★', notes: 'Referred by friend' },
                        { id: 'CLI-002', name: 'Mr. Okonkwo', type: 'Individual', contact: '+234 802 345 6789', email: 'okonkwo@email.com', totalSpent: 75000, commissionCount: 1, rating: '★★★★☆', notes: 'Wants annual family portrait' }
                    ]);
                    this.set('pricing', [
                        { service: 'Hyperrealistic Portrait (Single)', price: 75000, timeline: '2-3 weeks', addon: 'N/A' },
                        { service: 'Hyperrealistic Portrait (Couple)', price: 110000, timeline: '3-4 weeks', addon: 'N/A' },
                        { service: 'Family Portrait (3-4 subjects)', price: 150000, timeline: '4-5 weeks', addon: '+₦25k per extra subject' },
                        { service: 'Pet Portrait', price: 45000, timeline: '1-2 weeks', addon: 'N/A' },
                        { service: 'Live Event Painting', price: 80000, timeline: 'Same day', addon: 'N/A' },
                        { service: 'Gallery Exhibition Piece', price: 200000, timeline: '4-6 weeks', addon: 'N/A' }
                    ]);
                    localStorage.setItem('ajames_initialized', 'true');
                }
            }
        };

        let currentUser = null, currentModal = null, editingIndex = null;

        function showRegister() { document.getElementById('loginForm').style.display = 'none'; document.getElementById('registerForm').style.display = 'block'; }
        function showLogin() { document.getElementById('loginForm').style.display = 'block'; document.getElementById('registerForm').style.display = 'none'; }

        async function register() {
            const name = document.getElementById('regName').value, email = document.getElementById('regEmail').value, password = document.getElementById('regPassword').value;
            const errorDiv = document.getElementById('registerError'), successDiv = document.getElementById('registerSuccess');
            if (!name || !email || !password) { errorDiv.textContent = 'Please fill in all fields'; errorDiv.style.display = 'block'; return; }
            if (password.length < 6) { errorDiv.textContent = 'Password must be at least 6 characters'; errorDiv.style.display = 'block'; return; }
            document.getElementById('registerBtn').disabled = true;
            await new Promise(r => setTimeout(r, 1000));
            localStorage.setItem('ajames_user', JSON.stringify({ email, name }));
            errorDiv.style.display = 'none'; successDiv.textContent = 'Account created! Please sign in.'; successDiv.style.display = 'block';
            setTimeout(() => { showLogin(); document.getElementById('loginEmail').value = email; successDiv.style.display = 'none'; document.getElementById('registerBtn').disabled = false; }, 2000);
        }

        async function login() {
            const email = document.getElementById('loginEmail').value, password = document.getElementById('loginPassword').value;
            const errorDiv = document.getElementById('loginError');
            if (!email || !password) { errorDiv.textContent = 'Please enter email and password'; errorDiv.style.display = 'block'; return; }
            document.getElementById('loginBtn').disabled = true;
            await new Promise(r => setTimeout(r, 800));
            const savedUser = localStorage.getItem('ajames_user');
            currentUser = savedUser ? JSON.parse(savedUser) : { email: email || 'ajames@artist.com', name: 'A. James' };
            localStorage.setItem('ajames_user', JSON.stringify(currentUser));
            showDashboard();
        }

        function logout() { currentUser = null; document.getElementById('loginScreen').style.display = 'flex'; document.getElementById('dashboard').style.display = 'none'; }

        function showDashboard() {
            document.getElementById('loginScreen').style.display = 'none';
            document.getElementById('dashboard').style.display = 'block';
            document.getElementById('userEmail').textContent = currentUser?.name || currentUser?.email || 'A. James';
            DataStore.init(); updateDashboard();
        }

        function updateDashboard() {
            const commissions = DataStore.get('commissions'), expenses = DataStore.get('expenses'), inventory = DataStore.get('inventory');
            const totalRevenue = commissions.reduce((sum, c) => sum + (c.price || 0), 0);
            const outstanding = commissions.reduce((sum, c) => sum + (c.balance || 0), 0);
            const activeCount = commissions.filter(c => c.status === 'In Progress' || c.status === 'Scheduled').length;
            const totalExpenses = expenses.reduce((sum, e) => sum + (e.amount || 0), 0);
            document.getElementById('totalRevenue').textContent = '₦' + totalRevenue.toLocaleString();
            document.getElementById('outstandingPayments').textContent = '₦' + outstanding.toLocaleString();
            document.getElementById('activeCommissions').textContent = activeCount;
            document.getElementById('totalExpenses').textContent = '₦' + totalExpenses.toLocaleString();
            document.getElementById('recentCommissionsTable').innerHTML = commissions.slice(0, 5).map(c => `<tr><td><strong>${c.client}</strong></td><td>${c.artworkType}</td><td>₦${(c.price || 0).toLocaleString()}</td><td><span class="status-badge status-${c.status.toLowerCase().replace(/\\s/g, '-')}">${c.status}</span></td><td>${c.dueDate}</td></tr>`).join('') || '<tr><td colspan="5" style="text-align:center;padding:2rem;">No commissions yet</td></tr>';
            loadCommissionsTable(); loadExpensesTable(); loadInventoryGrid(); loadClientsTable(); loadPricing();
        }

        function loadCommissionsTable() {
            const commissions = DataStore.get('commissions');
            document.getElementById('commissionsTable').innerHTML = commissions.length ? commissions.map((c, i) => `<tr><td><strong>${c.id}</strong></td><td>${c.client}</td><td>${c.artworkType}</td><td>${c.medium}</td><td>₦${(c.price || 0).toLocaleString()}</td><td>₦${(c.deposit || 0).toLocaleString()}</td><td>₦${(c.balance || 0).toLocaleString()}</td><td><span class="status-badge status-${c.status.toLowerCase().replace(/\\s/g, '-')}">${c.status}</span></td><td><div class="action-btns"><button onclick="editCommission(${i})" class="btn-icon btn-edit"><i class="fas fa-edit"></i></button><button onclick="deleteCommission(${i})" class="btn-icon btn-delete"><i class="fas fa-trash"></i></button></div></td></tr>`).join('') : '<tr><td colspan="9" class="empty-state"><i class="fas fa-palette"></i><h3>No Commissions Yet</h3><p>Start tracking your art commissions here.</p></td></tr>';
        }

        function loadExpensesTable() {
            const expenses = DataStore.get('expenses');
            document.getElementById('expensesTable').innerHTML = expenses.length ? expenses.map((e, i) => `<tr><td>${e.date}</td><td><span class="status-badge" style="background:rgba(99,102,241,0.1);color:#6366f1;">${e.category}</span></td><td>${e.description}</td><td>${e.vendor}</td><td>₦${(e.amount || 0).toLocaleString()}</td><td>${e.receipt}</td><td><div class="action-btns"><button onclick="editExpense(${i})" class="btn-icon btn-edit"><i class="fas fa-edit"></i></button><button onclick="deleteExpense(${i})" class="btn-icon btn-delete"><i class="fas fa-trash"></i></button></div></td></tr>`).join('') : '<tr><td colspan="7" class="empty-state"><i class="fas fa-receipt"></i><h3>No Expenses Recorded</h3><p>Track your art supplies and business expenses.</p></td></tr>';
        }

        function loadInventoryGrid() {
            const inventory = DataStore.get('inventory');
            document.getElementById('inventoryGrid').innerHTML = inventory.length ? inventory.map((art, i) => `<div class="artwork-card"><div class="artwork-image"><i class="fas fa-image"></i></div><div class="artwork-info"><h3 class="artwork-title">"${art.title}"</h3><div class="artwork-meta">${art.medium} • ${art.size} • ${art.year}</div><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;"><span style="font-size:1.25rem;font-weight:700;">₦${(art.price || 0).toLocaleString()}</span><span class="status-badge" style="background:${art.status === 'Available' ? 'rgba(16,185,129,0.1)' : 'rgba(239,68,68,0.1)'};color:${art.status === 'Available' ? '#10b981' : '#ef4444'};">${art.status}</span></div><div class="action-btns" style="justify-content:flex-end;"><button onclick="editArtwork(${i})" class="btn-icon btn-edit"><i class="fas fa-edit"></i></button><button onclick="deleteArtwork(${i})" class="btn-icon btn-delete"><i class="fas fa-trash"></i></button></div></div></div>`).join('') : '<div class="empty-state" style="grid-column:1/-1;"><i class="fas fa-images"></i><h3>No Artworks in Inventory</h3><p>Add your available pieces for sale or exhibition.</p></div>';
        }

        function loadClientsTable() {
            const clients = DataStore.get('clients');
            document.getElementById('clientsTable').innerHTML = clients.length ? clients.map((c, i) => `<tr><td><strong>${c.name}</strong></td><td>${c.type}</td><td>${c.contact}</td><td>₦${(c.totalSpent || 0).toLocaleString()}</td><td>${c.commissionCount}</td><td>${c.rating}</td><td><div class="action-btns"><button onclick="editClient(${i})" class="btn-icon btn-edit"><i class="fas fa-edit"></i></button><button onclick="deleteClient(${i})" class="btn-icon btn-delete"><i class="fas fa-trash"></i></button></div></td></tr>`).join('') : '<tr><td colspan="7" class="empty-state"><i class="fas fa-users"></i><h3>No Clients Yet</h3><p>Build your client database here.</p></td></tr>';
        }

        function loadPricing() {
            const pricing = DataStore.get('pricing');
            document.getElementById('pricingGrid').innerHTML = pricing.map((p, i) => `<div class="pricing-card"><div class="pricing-header"><h3 class="pricing-title">${p.service}</h3><div class="pricing-amount">₦${(p.price || 0).toLocaleString()}</div></div><div class="pricing-note"><i class="fas fa-clock" style="margin-right:0.5rem;"></i>${p.timeline}</div>${p.addon !== 'N/A' ? `<div class="pricing-note" style="margin-top:0.5rem;"><i class="fas fa-plus-circle" style="margin-right:0.5rem;"></i>${p.addon}</div>` : ''}</div>`).join('');
        }

        function showSection(sectionId) {
            document.querySelectorAll('.content-section').forEach(s => s.classList.remove('active'));
            document.getElementById(sectionId).classList.add('active');
            document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
            event.target.closest('.nav-link').classList.add('active');
        }

        function openModal(type, index = null) {
            currentModal = type; editingIndex = index;
            const titles = { commission: 'Commission', expense: 'Expense', artwork: 'Artwork', client: 'Client' };
            document.getElementById('modalTitle').textContent = (index !== null ? 'Edit ' : 'New ') + titles[type];
            const forms = {
                commission: `<div class="form-row"><div class="form-group"><label>Client Name</label><input type="text" id="commClient" class="form-control"></div><div class="form-group"><label>Contact</label><input type="text" id="commContact" class="form-control"></div></div><div class="form-row"><div class="form-group"><label>Artwork Type</label><select id="commType" class="form-control"><option>Hyperrealistic Portrait</option><option>Family Portrait</option><option>Pet Portrait</option><option>Live Event Painting</option><option>Gallery Exhibition Piece</option></select></div><div class="form-group"><label>Medium</label><select id="commMedium" class="form-control"><option>Charcoal & Graphite</option><option>Oil on Canvas</option><option>Acrylic on Canvas</option><option>Colored Pencil</option><option>Watercolor</option></select></div></div><div class="form-row"><div class="form-group"><label>Size</label><input type="text" id="commSize" class="form-control"></div><div class="form-group"><label>Status</label><select id="commStatus" class="form-control"><option>Scheduled</option><option>In Progress</option><option>Completed</option></select></div></div><div class="form-row"><div class="form-group"><label>Total Price (₦)</label><input type="number" id="commPrice" class="form-control"></div><div class="form-group"><label>Deposit (₦)</label><input type="number" id="commDeposit" class="form-control"></div></div><div class="form-row"><div class="form-group"><label>Due Date</label><input type="date" id="commDueDate" class="form-control"></div><div class="form-group"><label>Completion Date</label><input type="date" id="commCompleteDate" class="form-control"></div></div>`,
                expense: `<div class="form-row"><div class="form-group"><label>Date</label><input type="date" id="expDate" class="form-control"></div><div class="form-group"><label>Category</label><select id="expCategory" class="form-control"><option>Art Supplies</option><option>Studio Equipment</option><option>Marketing</option><option>Transportation</option><option>Professional Services</option></select></div></div><div class="form-group full-width"><label>Description</label><input type="text" id="expDesc" class="form-control"></div><div class="form-row"><div class="form-group"><label>Vendor</label><input type="text" id="expVendor" class="form-control"></div><div class="form-group"><label>Amount (₦)</label><input type="number" id="expAmount" class="form-control"></div></div><div class="form-row"><div class="form-group"><label>Payment Method</label><select id="expMethod" class="form-control"><option>Bank Transfer</option><option>Cash</option><option>Card</option></select></div><div class="form-group"><label>Receipt #</label><input type="text" id="expReceipt" class="form-control"></div></div>`,
                artwork: `<div class="form-group full-width"><label>Title</label><input type="text" id="artTitle" class="form-control"></div><div class="form-row"><div class="form-group"><label>Medium</label><select id="artMedium" class="form-control"><option>Charcoal</option><option>Graphite</option><option>Oil on Canvas</option><option>Acrylic on Canvas</option><option>Watercolor</option></select></div><div class="form-group"><label>Size</label><input type="text" id="artSize" class="form-control"></div></div><div class="form-row"><div class="form-group"><label>Year</label><input type="number" id="artYear" class="form-control"></div><div class="form-group"><label>Status</label><select id="artStatus" class="form-control"><option>Available</option><option>Sold</option><option>Reserved</option></select></div></div><div class="form-row"><div class="form-group"><label>Price (₦)</label><input type="number" id="artPrice" class="form-control"></div><div class="form-group"><label>Location</label><input type="text" id="artLocation" class="form-control"></div></div>`,
                client: `<div class="form-row"><div class="form-group"><label>Name</label><input type="text" id="cliName" class="form-control"></div><div class="form-group"><label>Type</label><select id="cliType" class="form-control"><option>Individual</option><option>Gallery/Business</option><option>Organization</option></select></div></div><div class="form-row"><div class="form-group"><label>Contact</label><input type="text" id="cliContact" class="form-control"></div><div class="form-group"><label>Email</label><input type="email" id="cliEmail" class="form-control"></div></div><div class="form-group full-width"><label>Notes</label><textarea id="cliNotes" class="form-control" rows="3"></textarea></div>`
            };
            document.getElementById('modalBody').innerHTML = forms[type];
            document.getElementById('dataModal').classList.add('active');
            if (index !== null) populateForm(type, index);
            else if (type === 'commission') document.getElementById('commDueDate').valueAsDate = new Date();
            else if (type === 'expense') document.getElementById('expDate').valueAsDate = new Date();
            else if (type === 'artwork') document.getElementById('artYear').value = new Date().getFullYear();
        }

        function populateForm(type, index) {
            const data = DataStore.get(type === 'artwork' ? 'inventory' : type === 'client' ? 'clients' : type + 's');
            const item = data[index];
            if (type === 'commission') {
                document.getElementById('commClient').value = item.client || ''; document.getElementById('commContact').value = item.contact || '';
                document.getElementById('commType').value = item.artworkType || ''; document.getElementById('commMedium').value = item.medium || '';
                document.getElementById('commSize').value = item.size || ''; document.getElementById('commStatus').value = item.status || '';
                document.getElementById('commPrice').value = item.price || ''; document.getElementById('commDeposit').value = item.deposit || '';
                document.getElementById('commDueDate').value = item.dueDate || ''; document.getElementById('commCompleteDate').value = item.completionDate || '';
            } else if (type === 'expense') {
                document.getElementById('expDate').value = item.date || ''; document.getElementById('expCategory').value = item.category || '';
                document.getElementById('expDesc').value = item.description || ''; document.getElementById('expVendor').value = item.vendor || '';
                document.getElementById('expAmount').value = item.amount || ''; document.getElementById('expMethod').value = item.paymentMethod || '';
                document.getElementById('expReceipt').value = item.receipt || '';
            } else if (type === 'artwork') {
                document.getElementById('artTitle').value = item.title || ''; document.getElementById('artMedium').value = item.medium || '';
                document.getElementById('artSize').value = item.size || ''; document.getElementById('artYear').value = item.year || '';
                document.getElementById('artStatus').value = item.status || ''; document.getElementById('artPrice').value = item.price || '';
                document.getElementById('artLocation').value = item.location || '';
            } else if (type === 'client') {
                document.getElementById('cliName').value = item.name || ''; document.getElementById('cliType').value = item.type || '';
                document.getElementById('cliContact').value = item.contact || ''; document.getElementById('cliEmail').value = item.email || '';
                document.getElementById('cliNotes').value = item.notes || '';
            }
        }

        function closeModal() { document.getElementById('dataModal').classList.remove('active'); currentModal = null; editingIndex = null; }

        function saveData() {
            if (!currentModal) return;
            const btn = document.getElementById('saveBtn'); btn.innerHTML = '<span class="loading"></span> Saving...'; btn.disabled = true;
            setTimeout(() => {
                let data, key, newItem;
                if (currentModal === 'commission') {
                    key = 'commissions'; data = DataStore.get(key);
                    const price = parseFloat(document.getElementById('commPrice').value) || 0, deposit = parseFloat(document.getElementById('commDeposit').value) || 0;
                    newItem = { id: editingIndex !== null ? data[editingIndex].id : `COM-${Date.now()}`, client: document.getElementById('commClient').value, contact: document.getElementById('commContact').value, artworkType: document.getElementById('commType').value, medium: document.getElementById('commMedium').value, size: document.getElementById('commSize').value, status: document.getElementById('commStatus').value, price: price, deposit: deposit, balance: price - deposit, dueDate: document.getElementById('commDueDate').value, completionDate: document.getElementById('commCompleteDate').value, paymentStatus: deposit >= price ? 'Fully Paid' : deposit > 0 ? '50% Paid' : 'Pending' };
                } else if (currentModal === 'expense') {
                    key = 'expenses'; data = DataStore.get(key);
                    newItem = { id: editingIndex !== null ? data[editingIndex].id : `EXP-${Date.now()}`, date: document.getElementById('expDate').value, category: document.getElementById('expCategory').value, description: document.getElementById('expDesc').value, vendor: document.getElementById('expVendor').value, amount: parseFloat(document.getElementById('expAmount').value) || 0, paymentMethod: document.getElementById('expMethod').value, receipt: document.getElementById('expReceipt').value, deductible: true };
                } else if (currentModal === 'artwork') {
                    key = 'inventory'; data = DataStore.get(key);
                    newItem = { id: editingIndex !== null ? data[editingIndex].id : `ART-${Date.now()}`, title: document.getElementById('artTitle').value, medium: document.getElementById('artMedium').value, size: document.getElementById('artSize').value, year: parseInt(document.getElementById('artYear').value) || new Date().getFullYear(), status: document.getElementById('artStatus').value, price: parseFloat(document.getElementById('artPrice').value) || 0, location: document.getElementById('artLocation').value };
                } else if (currentModal === 'client') {
                    key = 'clients'; data = DataStore.get(key);
                    newItem = { id: editingIndex !== null ? data[editingIndex].id : `CLI-${Date.now()}`, name: document.getElementById('cliName').value, type: document.getElementById('cliType').value, contact: document.getElementById('cliContact').value, email: document.getElementById('cliEmail').value, notes: document.getElementById('cliNotes').value, totalSpent: editingIndex !== null ? data[editingIndex].totalSpent : 0, commissionCount: editingIndex !== null ? data[editingIndex].commissionCount : 0, rating: editingIndex !== null ? data[editingIndex].rating : '★★★★☆' };
                }
                if (editingIndex !== null) data[editingIndex] = newItem; else data.push(newItem);
                DataStore.set(key, data); updateDashboard(); closeModal(); showToast(editingIndex !== null ? 'Updated successfully!' : 'Added successfully!', 'success');
                btn.textContent = 'Save'; btn.disabled = false;
            }, 500);
        }

        function editCommission(index) { openModal('commission', index); }
        function deleteCommission(index) { if (confirm('Delete this commission?')) { const data = DataStore.get('commissions'); data.splice(index, 1); DataStore.set('commissions', data); updateDashboard(); showToast('Deleted', 'success'); } }
        function editExpense(index) { openModal('expense', index); }
        function deleteExpense(index) { if (confirm('Delete this expense?')) { const data = DataStore.get('expenses'); data.splice(index, 1); DataStore.set('expenses', data); updateDashboard(); showToast('Deleted', 'success'); } }
        function editArtwork(index) { openModal('artwork', index); }
        function deleteArtwork(index) { if (confirm('Delete this artwork?')) { const data = DataStore.get('inventory'); data.splice(index, 1); DataStore.set('inventory', data); updateDashboard(); showToast('Deleted', 'success'); } }
        function editClient(index) { openModal('client', index); }
        function deleteClient(index) { if (confirm('Delete this client?')) { const data = DataStore.get('clients'); data.splice(index, 1); DataStore.set('clients', data); updateDashboard(); showToast('Deleted', 'success'); } }

        function showToast(message, type = 'success') {
            const container = document.getElementById('toastContainer');
            const toast = document.createElement('div'); toast.className = `toast ${type}`;
            toast.innerHTML = `<i class="fas fa-${type === 'success' ? 'check-circle' : 'exclamation-circle'}"></i><span>${message}</span>`;
            container.appendChild(toast);
            setTimeout(() => { toast.style.opacity = '0'; toast.style.transform = 'translateX(100%)'; setTimeout(() => toast.remove(), 300); }, 3000);
        }

        document.getElementById('dataModal').addEventListener('click', function(e) { if (e.target === this) closeModal(); });
        document.addEventListener('keydown', function(e) { if (e.key === 'Escape') closeModal(); });
        document.addEventListener('DOMContentLoaded', function() { DataStore.init(); const savedUser = localStorage.getItem('ajames_user'); if (savedUser) { currentUser = JSON.parse(savedUser); showDashboard(); } });
    </script>
</body>
</html>'''

# Save the file
with open('/mnt/kimi/output/ajames_art_accounting.html', 'w', encoding='utf-8') as f:
    f.write(complete_html)

print("="*70)
print("✅ A. JAMES ART ACCOUNTING WEBSITE CREATED SUCCESSFULLY!")
print("="*70)
print("\n📁 FILE: ajames_art_accounting.html")
print("\n🌐 TO USE:")
print("   1. Open the HTML file in any web browser (Chrome, Firefox, Safari)")
print("   2. Create an account or use any demo credentials")
print("   3. Start managing your art business!")
print("\n💾 DATA STORAGE:")
print("   • All data saves to your browser's localStorage")
print("   • Data persists between sessions")
print("   • No internet required after first load")
print("\n🚀 TO DEPLOY ONLINE (FREE):")
print("   Option 1: Netlify (Recommended)")
print("   - Go to netlify.com")
print("   - Drag & drop the HTML file")
print("   - Get instant live URL")
print("\n   Option 2: Firebase")
print("   - Create account at firebase.google.com")
print("   - Install Firebase CLI: npm install -g firebase-tools")
print("   - Run: firebase init hosting")
print("   - Deploy: firebase deploy")
print("\n" + "="*70)
