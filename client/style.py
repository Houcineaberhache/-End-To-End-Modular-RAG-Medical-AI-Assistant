import streamlit as st


def inject_custom_css():
    st.markdown(
        """
        <style>
        /* ---------- Global ---------- */
        .stApp {
            background: linear-gradient(180deg, #0f1420 0%, #131a2b 100%);
        }

        /* ---------- Header ---------- */
        .medibot-header {
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 18px 0 6px 0;
        }
        .medibot-header .icon {
            font-size: 38px;
        }
        .medibot-header .title {
            font-size: 30px;
            font-weight: 700;
            color: #E8ECF4;
            margin: 0;
        }
        .medibot-header .subtitle {
            font-size: 14px;
            color: #8A93A8;
            margin-top: -2px;
        }
        .medibot-divider {
            border: none;
            border-top: 1px solid #232B3D;
            margin: 6px 0 18px 0;
        }

        /* ---------- Sidebar ---------- */
        section[data-testid="stSidebar"] {
            background-color: #10161F;
            border-right: 1px solid #232B3D;
        }
        section[data-testid="stSidebar"] h2 {
            color: #E8ECF4 !important;
            font-size: 18px !important;
        }

        /* ---------- Chat bubbles ---------- */
        div[data-testid="stChatMessage"] {
            border-radius: 14px;
            padding: 4px 6px;
            margin-bottom: 6px;
        }

        /* ---------- Source citation box ---------- */
        .source-box {
            background-color: #171F2E;
            border-left: 3px solid #4C8BF5;
            border-radius: 8px;
            padding: 10px 14px;
            margin-top: 8px;
            font-size: 13px;
            color: #A9B2C3;
        }
        .source-box b {
            color: #C7D0E0;
        }
        .source-chip {
            display: inline-block;
            background-color: #1E2A3F;
            color: #7FB2FF;
            border-radius: 6px;
            padding: 2px 8px;
            margin: 3px 4px 0 0;
            font-size: 12px;
            font-family: monospace;
        }

        /* ---------- Empty state ---------- */
        .empty-state {
            text-align: center;
            padding: 60px 20px;
            color: #6B7488;
        }
        .empty-state .big-icon {
            font-size: 46px;
            margin-bottom: 10px;
        }
        .empty-state .headline {
            font-size: 18px;
            color: #C7D0E0;
            font-weight: 600;
            margin-bottom: 4px;
        }

        /* ---------- Badge under title ---------- */
        .status-badge {
            display: inline-block;
            background-color: #17301F;
            color: #6FCF7E;
            border: 1px solid #244A31;
            border-radius: 20px;
            padding: 3px 12px;
            font-size: 12px;
            font-weight: 600;
            margin-top: 4px;
        }

        /* ---------- Disclaimer footer ---------- */
        .disclaimer {
            text-align: center;
            color: #565F73;
            font-size: 12px;
            margin-top: 30px;
            padding-top: 14px;
            border-top: 1px solid #1D2434;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )